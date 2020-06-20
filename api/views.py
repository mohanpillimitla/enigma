from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from .serializers import EmployeeSerializer

from .models import Employees


class ActivityView(generics.ListAPIView):

	
	def get_queryset(self):
		return Employees.objects.all()
	serializer_class=EmployeeSerializer

	

