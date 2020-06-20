
from django.urls import path
from .views import ActivityView

urlpatterns = [
  
    path('',ActivityView.as_view(),name='home'),


]