from click import password_option
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login


def webpage1(request):
    # print("YES")
    # print(request)
    # if request.method=='POST':
    #     print("YES")
    #     username=request.POST.get('username')
    #     pass1=request.POST.get('password')
    #     user=authenticate(request,username=username,password=pass1)
    #     #print("password", username, pass1)
    #     if user is not None:
    #         login(request,user)
    #         return redirect('webpage2')
    #     else:
    #         return HttpResponse("Username or Password is incorrect")
            
    return render(request,'login.html')

def webpage2(request):
   # print("YES")
    print(request)
    if request.method=='POST':
      #  print("YES")
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        if username in ['sajal','rashi','teacher']:
            request.session.flush()
            request.session['edit_access'] = 'true'
        else:
            request.session.flush()
            request.session['edit_access'] = 'false'
        user=authenticate(request,username=username,password=pass1)
            #print("password", username, pass1)
        if user is not None:
            login(request,user)
            return render(request,'main.html')
        else:
            return HttpResponse("Username or Password is incorrect")
    else:
         return render(request,'main.html')
        
def webpage3(request):
    return render(request,'timetable.html')

def webpage4(request):
    return render(request,'clssnewest.html')