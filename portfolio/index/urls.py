from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.home,name='home_path'),
    path('about/', views.aboutus,name='about_path'),
    path('contact/', views.contactus,name='contact_path'),
    path('employee/', include('employee.urls')),
]