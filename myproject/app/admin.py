from django.contrib import admin
from myproject.app import models


# Register your models here.
class MyModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.MyModel, MyModelAdmin)
