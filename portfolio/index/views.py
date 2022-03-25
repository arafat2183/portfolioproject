from django.shortcuts import render
from .models import about
from .models import slider
from .models import client
from .models import location
from .models import external_contact

def home(request):
    about_us_data = about.objects.all()
    slider_data = slider.objects.all()
    client_data = client.objects.all()
    print("my data:{}".format(about_us_data))
    context = {
        'about' : about_us_data,
        'slider' : slider_data,
        'client' : client_data
    }
    return render(request,'index.html',context)

def aboutus(request):
    return render(request,'about.html')

def contactus(request):
    info_data = location.objects.all()[0]
    context = {
        'information' : info_data,
    }
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        contactdata=external_contact(name=name,email=email,subject=subject,message=message)
        contactdata.save()
    return render(request,'contact.html',context)