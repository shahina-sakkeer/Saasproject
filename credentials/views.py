from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth

# Create your views here.

def register(request):
    if request.method=="POST":
        username=request.POST["username"]
        firstname=request.POST["first_name"]
        lastname=request.POST["last_name"]
        password=request.POST["password"]

        if User.objects.filter(username=username).exists():
            messages.info(request,"username is already taken")
            return redirect('credentials:signup')
        
        else:
            user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,password=password)
            user.save()
            messages.info(request,"registration completed")
            return redirect('credentials:signin')


    return render(request,"register.html")


def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('saasapp:demo')
        else:
            messages.info(request,"invalid username !!!")
            return redirect('credentials:signin')
    return render(request,"login.html")   

