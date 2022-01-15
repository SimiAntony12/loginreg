from django.contrib.auth.models import Group, User
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from .decorators import admin_only
# Create your views here.

@login_required(login_url='loginPage') #loginpage udegil
@admin_only
def home(request):
    return render(request,'home.html')

def register(request):
    form=CreateUserForm()
    context={'form':form}
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            group=request.POST.get('groups')
            user.groups.add(group)
            return redirect('home')
    return render(request,'register.html',context)  

def loginPage(request):
    if request.method == 'POST':
        username=request.POST.get('user')
        password=request.POST.get('pass')
        user= authenticate(request,username=username,password=password)
        if user is not None:     #user undegil
            login(request,user)
            return redirect('home')
        else:
            return redirect('loginPage')    

    return render(request,'login.html')
    #return HttpResponse('loginpage') 

def logoutPage(request):
    logout(request)
    return redirect('loginPage')    

def teacher(request):
    data=User.objects.get(id=request.user.id)
    context={'data':data}
    return render(request,'teacher.html',context)
    
def student(request):
    data=User.objects.get(id=request.user.id)
    context={'data':data}
    return render(request,'student.html',context)
       