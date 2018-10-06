from django.contrib import admin
from testcase.models import TestCase, CaseModule, TestSuite, SuitCaseMapping

# Register your models here.

admin.site.register(TestCase)
admin.site.register(CaseModule)
admin.site.register(TestSuite)
admin.site.register(SuitCaseMapping)
