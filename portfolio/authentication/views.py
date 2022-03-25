from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib import User

def authlogin(request):
    if request.method=='POST':
        name=request.POST['name']
        password=request.POST['password']
        user=authenticate(request, username=name, password=password)
        if user is not None:
            login(request,user)
            return redirect('profile_url')
        else:
            messages.error(request, 'Invalid Username and Password!')
    return render(request,'authentication/login.html')


def authregistration(request):
    if request.method=='POST':
        name=request.POST['name']    
        email=request.POST['email']    
        password=request.POST['password']    
        confirm_password=request.POST['confirm_password']
        if password==confirm_password:
           if User.objects.filter(username=name).exists():
               messages.error(request, 'This Username already exist!Please try another Username')
           elif User.objects.filter(email=email).exists():
               messages.error(request, 'This Email already exist!Please try another Username')
           else:
               user=User.objects.create_user(username=name, password=password, email=email)
               user.save()
               return redirect('login_path')
        else:
          messages.error(request, 'Password and Confirm Password does not matched!')      
    return render(request,'authentication/registration.html')


def forgotpassword(request):
    
    return render(request,'authentication/forgot.html')


def userlogout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully!')
    return redirect('login_path')