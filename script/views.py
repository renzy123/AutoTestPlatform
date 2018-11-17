import time

from django.http import JsonResponse
from django.shortcuts import render, redirect

from AutoTestPlatform.CommonModels import SqlResultData, ResultEnum, result_to_json
from product.models import Product
from script.dataModels import ScriptData
from script.form import ScriptUploadForm
from script.models import Script
from script.models import ScriptType
from testcase.models import SuiteScriptMapping, TestSuite
from testcase.models import TestCase
from user.models import User
from utils.utilsFunc import *
from utils.utilsFunc import gen_data_json


# Create your views here.


def init_upload_page(request, suite_id=None):
    """初始化测试用例列表页面的显示方式"""
    if request.method == "GET":
        """
        当请求方式为GET时，初始化测试用例页面的显示，该页面为/pages/testcase/scripts.html
        首先请求用例模组，然后根据用例模组初始化用例列表
        """
        # 获取product列表
        # 获取脚本的分类列表
        script_types = [s_type for s_type in ScriptType.objects.all()]
        products = Product.objects.all()
        return render(request, "pages/script/upload.html",
                      {"types": script_types, "products": products})
    if request.method == "POST":
        """请求方式为POST，即为提交脚本数据"""
        upload_form = ScriptUploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            cleaned_data = upload_form.cleaned_data
            script_file = cleaned_data["scriptFile"]
            title = cleaned_data["title"]
            suite = cleaned_data["suite"]
            script_type = cleaned_data["scriptType"]
            desc = cleaned_data["desc"]
            # 将脚本保存到制定的目录下
            title_and_path = _create_script_file(script_file, script_type)
            if not title_and_path:
                result = SqlResultData(ResultEnum.Error, "插入数据库失败！")
                return JsonResponse(result_to_json(result))
            # 生成Script对象并且将其保存到数据库
            script = Script()
            script.title = title
            script.path = title_and_path[1]
            user = request.session[SESSION_USER_NAME]
            user_id = User.objects.filter(name=user)[0].id
            script.create_user = user_id
            script.last_edit_user = user_id
            script.desc = desc
            script.script_type = script_type
            try:
                script.save()
                # 如果suite!=-1，那写映射关系表
                if suite != -1:
                    script_id = script.id
                    _map = SuiteScriptMapping()
                    _map.suite = suite
                    _map.script = script_id
                    _map.save()
            except ValueError:
                result = SqlResultData(ResultEnum.Error, "插入数据库失败！")
                return JsonResponse(result_to_json(result))
            else:
                return redirect("/testcase/list")
        else:
            print(upload_form.errors)


def script_of_case(request):
    """在CASE列表页异步请求脚本的信息的请求"""
    result = Script.objects.filter(related_case=request.session[SESSION_CASE_ID])
    if result.count() == 0:
        return JsonResponse({"res": "no"})
    script = result[0]
    data = {"res": "yes", "id": script.id, "title": script.title, "code": read_scripts(script.path)}
    return JsonResponse(data)


def init_scripts(request, _type=None):
    """构建脚本列表页面"""
    if request.method == "GET":
        # 初始化页面
        # 获取所有的脚本信息
        scripts = Script.objects.all()
        script_info = []
        selected_type = _type
        if selected_type:
            scripts = scripts.filter(script_type=selected_type)
            selected_type = ScriptType.objects.filter(id=selected_type)[0].name
        for script in scripts:
            """获取脚本的所有信息"""
            script_type = ScriptType.objects.filter(id=script.script_type)[0].name
            create_user = User.objects.filter(id=script.create_user)[0].real_name
            editor = User.objects.filter(id=script.last_edit_user)[0].real_name
            suites = SuiteScriptMapping.objects.filter(script=script.id)
            # 获取套件相关的信息
            suites_info = {}
            for suite in suites:
                suites_info[suite] = TestSuite.objects.filter(id=suite)[0].title
            info = gen_data_json(script,
                                 {"script_type": script_type, "create_user": create_user, "editor": editor,
                                  "suites_info": suites_info})
            script_info.append(info)
        # 获取分类信息
        script_types = ScriptType.objects.all()
        return render(request, "pages/script/scripts.html",
                      {"script_info": script_info, "script_types": script_types, "selected_type": selected_type})
    if request.method == "POST":
        # 处理AJAX请求
        scripts = Script.objects.all()
        scripts = [serialize_model(ScriptData(script)) for script in scripts]
        script_types = ScriptType.objects.all()
        script_types = [serialize_model(sType) for sType in script_types]
        data = {"scripts": scripts, "types": script_types}
        return JsonResponse(data)


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
        return title + ".py", os.path.join(s_type, file_name)
