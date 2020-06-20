from rest_framework import serializers
from .models import Employees,Activities






class ActivitySerializer(serializers.ModelSerializer):

	class Meta:
		model=Activities

		fields=['start_time','end_time',]



class EmployeeSerializer(serializers.ModelSerializer):
	activity=ActivitySerializer(many=True)
	class Meta:
		model=Employees

		fields=['id','real_name','tz','activity']





