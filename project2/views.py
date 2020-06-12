from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.

def home(request,*args, **kwargs):
  return render(request,'base.htm',{})

def logoutview(request,*args,**kwargs):
  logout(request)
  return redirect('home')

def registerview(request,*args,**kwargs):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      # username = form.cleaned_data.get('username')
      # raw_password = form.cleaned_data.get('password')
      # user = authenticate(username=username,password=raw_password)
      if user is not None:
        login(request,user)
        return redirect('home')
      else:
        print('could not register')
        return redirect('register')
  else:
    form = UserCreationForm()
  return render(request,'register.htm',{
    'form':form
  })

