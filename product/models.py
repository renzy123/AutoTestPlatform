from django.db import models


# Create your models here.


class Product(models.Model):
    """
    各个字段的说明：
    name:产品名
    user_in_charge:产品的负责人
    create_user:产品的创建者
    create_time:产品的创建时间
    description:产品的描述
    """
    name = models.CharField(max_length=255, unique=True, null=False)
    inChargeUser = models.IntegerField(null=False)
    createUser = models.IntegerField(null=False)
    createTime = models.DateField(auto_now=True)
    desc = models.TextField()
    status = models.IntegerField(null=False, default=1)
    manager = models.CharField(max_length=50, default="暂无")


class Status(models.Model):
    """
    产品状态表
    status:产品的状态
    desc:该状态的具体描述
    """
    status = models.CharField(max_length=40, unique=True, null=False)
    desc = models.TextField()


class SuitProductMapping(models.Model):
    """测试套件和产品的关联类"""
    product = models.IntegerField()
    suit = models.IntegerField()
