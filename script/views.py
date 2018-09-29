import time

from django.http import JsonResponse
from django.shortcuts import render

from AutoTestPlatform.CommonModels import SqlResultData, ResultEnum, result_to_json
from script.form import ScriptUploadForm
from script.models import ScriptType, Script
from testcase.models import CaseModule
from testcase.models import TestCase
from user.models import User
from utils.consts import *


# Create your views here.


def init_upload_page(request):
    """初始化测试用例列表页面的显示方式"""
    if request.method == "GET":
        """
        当请求方式为GET时，初始化测试用例页面的显示，该页面为/pages/testcase/list.html
        首先请求用例模组，然后根据用例模组初始化用例列表
        """
        module_queryset = CaseModule.objects.all()
        module_dict = dict(
            [(m.id, m) for m in module_queryset]
        )
        # 获取脚本的分类列表
        script_types = [s_type for s_type in ScriptType.objects.all()]
        # 在/storage/scripts/目录下创建各个脚本分类的文件夹
        _create_script_folder()
        # 请求用例列表
        case_queryset = TestCase.objects.all()
        # 根据用例列表来进行分组，生成DICT
        module_case_dict = {}
        for _id in module_dict.keys():
            case_list = [case for case in case_queryset if case.case_module == _id]
            module_case_dict[module_dict.get(_id).name] = case_list
        # 传输数据说明：
        # module_case_list：NAME:LIST
        # user_dict：用户ID:NAME 字典
        # first_case：第一个需要显示的case
        # 将当前操作的测试用例ID写入到session
        return render(request, "pages/script/upload.html",
                      {"module_case_dict": module_case_dict, "types": script_types})
    if request.method == "POST":
        """请求方式为POST，即为提交脚本数据"""
        print(request.FILES)
        upload_form = ScriptUploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            cleaned_data = upload_form.cleaned_data
            script_file = cleaned_data["scriptFile"]
            script_case = cleaned_data["case"]
            script_type = cleaned_data["scriptType"]
            desc = cleaned_data["desc"]
            # 将脚本保存到制定的目录下
            title_and_path = _create_script_file(script_file, script_type)
            if not title_and_path:
                result = SqlResultData(ResultEnum.Error, "插入数据库失败！")
                return JsonResponse(result_to_json(result))
            # 生成Script对象并且将其保存到数据库
            script = Script()
            script.title = title_and_path[0]
            script.path = title_and_path[1]
            user = request.session[SESSION_USER_NAME]
            user_id = User.objects.filter(name=user)[0].id
            script.create_user = user_id
            script.last_edit_user = user_id
            script.desc = desc
            script.related_case = TestCase.objects.filter(title=script_case)[0].id
            script.script_type = script_type
            try:
                script.save()
            except ValueError:
                result = SqlResultData(ResultEnum.Error, "插入数据库失败！")
                return JsonResponse(result_to_json(result))
            else:
                result = SqlResultData(ResultEnum.Success, "插入数据库失败！")
                return JsonResponse(result_to_json(result))
        else:
            print(upload_form.errors)


def init_scripts_list(request):
    """构建脚本列表页面"""
    if request.method == "GET":
        # 初始化页面

        pass
    if request.method == "POST":
        # 处理AJAX请求
        pass


def find_script_with_case(request):
    """使用caseID/title来获取script的信息"""
    """请求方式：GET"""
    if request.method == "GET":
        data = request.GET["case"]
        if str(data).isdigit():
            case_id = data
        else:
            case_id = TestCase.objects.filter(title=data)[0].id
        script_of_case = Script.objects.filter(case_id=case_id)[0]
        with open(script_of_case.path, mode="r") as f:
            content = f.readlines()[:-1]
        return JsonResponse(request, {"id": script_of_case.id, "content": content})


def _create_script_folder():
    """初始化脚本的各个文件夹"""
    script_types = ScriptType.objects.all()
    dirs = [os.path.join(SCRIPT_DIR, type_dir.name) for type_dir in script_types]
    for a_dir in dirs:
        if os.path.exists(a_dir):
            continue
        else:
            os.mkdir(a_dir)


def _create_script_file(file, s_type):
    """在指定的目录下创建文件
        为了解决重名问题，所有的文件在传输到服务器后，名称将统一变为name+当前毫秒数+后缀名的方式
    """
    s_type = ScriptType.objects.filter(id=s_type)[0].name
    index_of_suffix = str(file.name).rindex(".")
    title = file.name[:index_of_suffix]
    file_name = title + str(int(time.time() * 1000)) + file.name[
                                                       index_of_suffix:]
    new_file_path = os.path.join(os.path.join(SCRIPT_DIR, s_type), file_name)
    try:
        new_file = open(new_file_path, "w", encoding="utf-8")
        # 读取内存中保存的文件
        if file.multiple_chunks():
            for chunk in file.chunks():
                new_file.write(chunk)
        else:
            new_file.write(file.read().decode("utf-8"))
        new_file.flush()
        new_file.close()
    except ValueError:
        return False
    else:
        return title + ".py", new_file_path
