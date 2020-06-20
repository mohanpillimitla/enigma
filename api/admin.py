from django.contrib import admin

# Register your models here.
from .models import Employees,Activities

admin.site.register([Employees,Activities])