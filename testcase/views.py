import json

from django.http import JsonResponse
from django.shortcuts import render, redirect

from AutoTestPlatform.CommonModels import ResultEnum, SqlResultData, result_to_json
from product import views as pViews
from testcase import form
from testcase.dataModels import TestCaseData, TestCaseDetail
from testcase.models import TestCase, CaseModule, TestSuite, SuitCaseMapping
from user.models import User
from user.userUtils import user_dict
from utils.consts import *
from django.utils.datastructures import MultiValueDictKeyError
from utils.utilsFunc import read_scripts, gen_data_json
from script.models import Script
from product.models import Product, SuitProductMapping, Status


# Create your views here.





def module_dict():
    """
    :return: 模组的ID：模组的对应表
    """
    modules = CaseModule.objects.all()
    return dict([
        (mod.id, mod) for mod in modules
    ])


def init_upload_page(request):
    if request.method == "GET":
        # 从session中获取当前登录的用户
        name = request.session.get(SESSION_USER_NAME)
        # 获取所有的产品列表，然后传回并且生成select列表
        product_query_set = Product.objects.all()
        products = [product.name for product in product_query_set]
        # 获取第一个产品的相关详细信息，并且传递到前端页面
        first_product = pViews.product_detail_no_request(products[0])
        return render(request, "pages/testcase/upload.html",
                      {"user": name, "products": products, "relatedData": first_product})
    if request.method == "POST":
        pass


def init_case_list(request):
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
        users_dict = user_dict()
        # 请求用例列表
        case_queryset = TestCase.objects.all()
        first_case = ""
        # 根据用例列表来进行分组，生成DICT
        module_case_dict = {}
        for _id in module_dict.keys():
            case_list = [case for case in case_queryset if case.case_module == _id]
            if first_case == "" and len(case_list) != 0:
                first_case = case_list[0]
            module_case_dict[module_dict.get(_id).name] = case_list
        # 获取一个待显示的Case信息
        first_case = case_queryset.filter(id=first_case.id)[0]
        # 传输数据说明：
        # module_case_list：NAME:LIST
        # user_dict：用户ID:NAME 字典
        # first_case：第一个需要显示的case
        # 将当前操作的测试用例ID写入到session
        request.session[SESSION_CASE_ID] = first_case.id
        first_case_detail = TestCaseDetail(first_case)
        first_case = TestCaseData(first_case, users_dict, module_dict)

        return render(request, "pages/testcase/list.html",
                      {"module_case_dict": module_case_dict, "first_case": first_case,
                       "first_case_detail": first_case_detail
                       })


def case_data(request):
    """用于异步请求测试用例的数据"""
    global _case
    """请求需要测试用例的ID"""
    if request.method == "GET":
        case_id = request.GET.get("id")
        case = TestCase.objects.filter(id=case_id)
        if len(case) == 0:
            return
        case = case[0]
        caseData = TestCaseData(case, user_dict(), module_dict())
        caseData_dict = caseData.__dict__
        caseData_dict.pop("_state")
        data = {"caseData": caseData_dict}
        caseDetail = TestCaseDetail(case)
        data["caseDetail"] = caseDetail.__dict__
        # 将当前操作的测试用例ID写入到session
        request.session[SESSION_CASE_ID] = case.id
        # 返回数据
        return JsonResponse(data)
    if request.method == "POST":
        """此处进行测试用例的删除"""
        caseData = request.POST.get("caseData")
        _case = TestCase.objects.filter(id=request.session[SESSION_CASE_ID])[0]
        caseData = json.loads(caseData)
        _case.title = caseData["title"]  # 更新前置条件
        pres = caseData["pres"]
        pres_string = " "
        pres_string = pres_string.join(pres)
        _case.precondition = pres_string
        # 修改步骤和期望
        steps = caseData["steps"]
        expects = caseData["expects"]
        step_string = " ".join(steps)
        expects_string = " ".join(expects)
        _case.steps = step_string
        _case.expect = expects_string
        # 修改updateUser和updateTime
        user_name = request.session[SESSION_USER_NAME]
        _case.last_edit_user = User.objects.filter(name=user_name)[0].id
    try:
        _case.save()
    except ValueError as error:
        print(error.__str__())
        result = SqlResultData(ResultEnum.Error, "修改失败，请回报任宗毅！")
        return JsonResponse(result_to_json(result))
    else:
        result = SqlResultData(ResultEnum.Success)
        return JsonResponse(result_to_json(result))


def init_case_detail(request):
    """初始化测试用例详情页面"""
    if request.method == "GET":
        """
        当请求方式为GET时，初始化测试用例页面的显示，该页面为/pages/testcase/modCase.html
        """
        users_dict = user_dict()
        # 请求用例列表
        first_case = TestCase.objects.filter(id=request.session[SESSION_CASE_ID])[0]
        # 传输数据说明：
        # module_case_list：NAME:LIST
        # user_dict：用户ID:NAME 字典
        # first_case：第一个需要显示的case
        # 将当前操作的测试用例ID写入到session
        request.session[SESSION_CASE_ID] = first_case.id
        first_case_detail = TestCaseDetail(first_case)
        first_case = TestCaseData(first_case, users_dict, module_dict())
        return render(request, "pages/testcase/modCase.html",
                      {"first_case": first_case,
                       "first_case_detail": first_case_detail
                       })


def init_suit_page(request, suite_id):
    """初始化测试用例详情页面"""
    if request.method == "GET":
        # 获取产品列表
        products = Product.objects.all()
        product_info = []
        for a_product in products:
            info = {"id": a_product.id, "name": a_product.name,
                    "inCharge": User.objects.filter(id=a_product.inChargeUser)[0].name,
                    "status": Status.objects.filter(id=a_product.status)[0].status}
            product_info.append(info)
        # 获取第测试套件列表
        suits = TestSuite.objects.all()
        # 是否有参数传入
        if suite_id != 0:
            suite = TestSuite.objects.filter(id=suite_id)[0]
        else:
            suite = TestSuite.objects.all()[0]

        user_create = User.objects.filter(id=suite.create_user)[0].real_name
        user_edit = User.objects.filter(id=suite.last_editer)[0].real_name
        suite_info = gen_data_json(suite, {"user_create": user_create, "user_edit": user_edit})
        # 关联的测试用例列表
        case_of_suite = []
        for case in [sc_map.case for sc_map in SuitCaseMapping.objects.filter(suit=suite.id)]:
            case_of_suite.append(TestCase.objects.filter(id=case)[0])

        # 关联的产品列表

        products_of_suite = []
        for product in [ps_map.product for ps_map in SuitProductMapping.objects.filter(suit=suite.id)]:
            products_of_suite.append(Product.objects.filter(id=product)[0])
        print(products_of_suite)

        # 关联的setup和TearDown

        setup = None
        teardown = None
        if suite.setup is not None:
            setup = Script.objects.filter(id=suite.setup)[0]
        if suite.teardown is not None:
            teardown = Script.objects.filter(id=suite.teardown)[0]

        return render(request, "pages/testcase/suite.html",
                      {"suits": suits, "suite_info": suite_info, "case_of_suite": case_of_suite,
                       "products_of_suite": products_of_suite, "setup": setup, "teardown": teardown,
                       "product_info": product_info})


def suit_info(request):
    """用于请求某一ID下的测试套件的详细信息"""
    try:
        suit_id = request.POST["suit_id"]
        suite = TestSuite.objects.filter(id=suit_id)[0]
        # 获取历史信息的字典
        history = {"creator": User.objects.filter(id=suite.create_user)[0].name, "create_time": suite.create_time,
                   "last_editor": User.objects.filter(id=suite.last_editer)[0].name,
                   "last_edit_time": suite.last_edit_time, "desc": suite.desc}
        # 获取setup和teardown
        s_t = {}
        if not suite.setup:
            s_t["setup"] = ""
        else:
            s_t["setup"] = read_scripts(Script.objects.filter(id=suite.setup)[0].path)
        if not suite.teardown:
            s_t["teardown"] = ""
        else:
            s_t["teardown"] = read_scripts(Script.objects.filter(id=suite.teardown)[0].path)
        # 获取测试用例列表
        case_ids = [case_map.case for case_map in SuitCaseMapping.objects.filter(suit=suite.id)]
        _case_data = []
        for case_id in case_ids:
            case = TestCase.objects.filter(id=case_id)[0]
            _case_data.append((case.id, case.title))
        # 获取关联的产品列表
        product_ids = [p_s_map.product for p_s_map in SuitProductMapping.objects.filter(suit=suite.id)]
        related_products = []
        for product_id in product_ids:
            product = Product.objects.filter(id=product_id)[0]
            related_products.append((product.id, product.name))

        suite_info = {"history": history, "setup_teardowns": s_t, "case_data": _case_data,
                      "related_products": related_products}
        return JsonResponse(suite_info)
    except MultiValueDictKeyError:
        return JsonResponse(result_to_json(SqlResultData(ResultEnum.Error, "请求方式错误!")))


def new_suit_page(request):
    """进行新建suit的方法"""
    module_queryset = CaseModule.objects.all()
    module_dict = dict(
        [(m.id, m) for m in module_queryset]
    )
    case_queryset = TestCase.objects.all()
    # 根据用例列表来进行分组，生成DICT
    module_case_dict = {}
    for _id in module_dict.keys():
        case_list = [case for case in case_queryset if case.case_module == _id]
        module_case_dict[module_dict.get(_id).name] = case_list
        # 传输数据说明：
        # module_case_list：NAME:LIST
    try:
        if request.GET["success"]:
            return render(request, "pages/testcase/newSuit.html",
                          {"module_case_dict": module_case_dict, "success": "yes"})
    except MultiValueDictKeyError:
        pass
    return render(request, "pages/testcase/newSuit.html",
                  {"module_case_dict": module_case_dict})


def new_suit(request):
    if request.method == "POST":
        """增加测试套件的方法"""
        suitForm = form.SuitForm(request.POST)
        if suitForm.is_valid():
            data = suitForm.cleaned_data
            suitName = data["suitName"]
            setupId = data["setupId"]
            teardownId = data["tearDownId"]
            desc = data["desc"]
            caseList = data["caseList"]
            # 插入数据库
            suit = TestSuite()
            user = request.session[SESSION_USER_NAME]
            suit.create_user = User.objects.filter(name=user)[0].id
            suit.title = suitName
            suit.desc = desc if desc != "" else None
            # suit.setup = setupId if setupId != "" else None
            suit.last_editer = suit.create_user
            suit.run_count = 0
            # suit.teardown = teardownId
            suit.save()
            # 获取ID
            currrent_suit_id = suit.id
            # 插入suit case映射表
            case_list = str(caseList).split(";")[:-1]
            for case_id in case_list:
                suit_case_map = SuitCaseMapping()
                suit_case_map.suit = currrent_suit_id
                suit_case_map.case = case_id
                suit_case_map.save()
            return redirect("/testcase/newSuit?success=yes")
        else:
            return


def del_case(request, case_id=None):
    """
    删除当前操作的测试用例
    """
    if case_id:
        case_id = case_id
    else:
        case_id = request.session[SESSION_CASE_ID]
    # TestCase.objects.filter(id=case_id).delete()
    return redirect("/testcase/list/")


def is_case_exists(request, title=None):
    """判断某个测试用例是否存在"""
    if request.method == "GET":
        case_title = request.GET.get("title")
        if len(TestCase.objects.filter(title=case_title)) != 0:
            return JsonResponse({"result": "true"})
        else:
            return JsonResponse({"result": "false"})
