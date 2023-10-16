from django.shortcuts import render

from click import password_option
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from flask import redirect
def webpage1(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('webpage2')
        else:
            return HttpResponse("Username or Password is incorrect")
            
    return render(request,'login.html')

def webpage2(request):
    return render(request,'main.html')

def webpage3(request):
    return render(request,'timetable.html')
# Create your views here.
