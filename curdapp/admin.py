from django.contrib import admin
from .models import Employeedata

class AdminEmployeedata(admin.ModelAdmin):
    list_display = ['First Name','Last Name','Email Id','Mobile ','Locations']
admin.site.register(Employeedata)
# Register your models here.
