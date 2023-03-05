
from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import message

def RegisterView(request):
    form = RegisterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return redirect('unsucces')
            
    form = RegisterForm()
    context = {
        'form':form
    }
    return render(request,'register.html',context)

def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return redirect('login_error')

    return render(request,'login.html',{})

def HomeView(request):
    username = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    msg = request.POST.get('message')

    conditions =[
        username is not None,
        email is not None,
        subject is not None,
        msg is not None,
    ]
    if all(conditions):
        message.objects.create(username=username ,email=email, subject=subject, msg=msg)
    return render(request,'home.html',{})

def logoutView(request):
    logout(request)
    return redirect('login')

def unsucces(request):
    return render(request,'unsucces.html',{})

def login_err(request):
    return render(request,'unsucces-login.html',{})

@login_required
def dashboard(request):
    return render(request,'dashboard.html',{})

@login_required
def userpanel(request):
    context = {
        'users':User.objects.all()
    }
    return render(request,'users.html', context)

@login_required
def messagepanel(request):
    context = {
        'message':message.objects.all()
    }
    return render(request,'messages.html',context)