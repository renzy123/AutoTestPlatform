from django.contrib import admin
from script.models import Script, ScriptType

# Register your models here.

admin.site.register(ScriptType)
admin.site.register(Script)
