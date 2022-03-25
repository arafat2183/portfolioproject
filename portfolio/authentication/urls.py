from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.authlogin, name='login_path'),
    path('registration/', views.authregistration, name='registration_path'),
    path('forgot-password/', views.forgotpassword, name='forgotpassword_path'),
    path('logout/', views.userlogout, name='logout_path'),
]