from django.db import models


# Create your models here.


class TestCase(models.Model):
    """
    测试用例的数据模型
    字段说明：
    title:测试用例标题  text
    precondition: 前置条件 text
    steps:步骤
    expect:期望
    create_user:创建者 integer
    create_time:创建时间 dateTime
    last_edit_user:最后编辑者 integer
    last_edit_time:最后编辑时间 dateTime
    editable:可编辑状态 boolean
    case_module:所属模块 Integer
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=False)
    precondition = models.TextField(max_length=255, null=True)
    steps = models.TextField(null=False)
    expect = models.TextField(null=False)
    create_user = models.IntegerField(null=False)
    create_time = models.DateTimeField(auto_now_add=True)
    last_edit_user = models.IntegerField()
    last_edit_time = models.DateTimeField(auto_now=True)
    case_module = models.IntegerField()
    editable = models.BooleanField(default=True)


class CaseModule(models.Model):
    """
    模块的数据模型
    字段说明：
    name:模块名称
    create_time: 创建时间
    create_user: 创建者
    desc: 描述
    """
    name = models.CharField(max_length=255, unique=True)
    create_time = models.DateTimeField(auto_now=True)
    create_user = models.IntegerField()
    desc = models.TextField()


class TestSuite(models.Model):
    """测试套件描述类
    字段说明：
    title:标题
    create_time:创建时间
    create_user:创建者
    desc:说明描述
    setup:测试套件的setup脚本
    teardown:测试套件的teardown脚本
    """
    title = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    create_user = models.IntegerField()
    desc = models.CharField(max_length=100, null=True)
    setup = models.IntegerField(null=True)
    teardown = models.IntegerField(null=True)


class SuitCaseMapping(models.Model):
    """
    测试套件/测试用例映射表
    suit:测试套件ID
    case:测试用例ID
    desc:说明描述
    """
    suit = models.IntegerField()
    case = models.IntegerField()
    desc = models.CharField(max_length=100, null=True)
