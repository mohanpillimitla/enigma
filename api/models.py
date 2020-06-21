from django.db import models
from timezone_utils.fields import TimeZoneField
from timezone_utils.choices import PRETTY_ALL_TIMEZONES_CHOICES

# Create your models here.

class Employees(models.Model):
	id=models.CharField(max_length=10,primary_key=True)
	real_name=models.CharField(max_length=20)
	tz=TimeZoneField(choices=PRETTY_ALL_TIMEZONES_CHOICES)

	

class Activities(models.Model):
	employee=models.ForeignKey(Employees,on_delete=models.CASCADE,null=False,related_name='activity')

	start_time=models.DateTimeField()
	end_time=models.DateTimeField()
