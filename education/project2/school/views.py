from django.shortcuts import render , redirect
from django.http import HttpResponse
from school.models import Newuser
from django.contrib.auth import authenticate,login

def abc(request):
    return HttpResponse("hi")

def index(request):
    return render(request,"index.html")

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        # re_password=request.POST['re_password']

        user1=Newuser.objects.create_user(username=username,email=email,password=password)

        return redirect("loginn")
    
    return render(request,"register.html")

def loginn(request):
    if request.method=='POST':
        login_username=request.POST['login_username']
       
        login_password=request.POST['login_password']
      

        user=authenticate(username=login_username,password=login_password)

        if user is not None:
            login(request,user)

            return redirect("dash")
    return render(request,"handlelogin.html")

def dash(request):
    return render(request,'dash.html')

def students(request):
    data=Newuser.objects.all().values().filter(is_staff=False ,is_active=True,user_type="student")
    d={
        'data':data,
    }
    return render(request,'students.html',d)

def teacher(request):
    data=Newuser.objects.all().values().filter(is_staff=True ,is_active=True,user_type="Teacher")
    d={
        'data':data,
    }
    return render(request,'teacher.html',d)
# Create your views here.


