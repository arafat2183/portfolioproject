from django.shortcuts import render
from django.http import HttpResponse

def employee(request):
    return HttpResponse("This is our Employee Module page")

def profile(request):
    return render(request,'employee/profile.html')


