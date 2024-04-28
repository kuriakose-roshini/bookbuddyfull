from django.template import loader
from django.contrib.auth import authenticate, login as authlogin, logout as authlogout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Reader
from . import forms


def index(request):
        template = loader.get_template('index.html')
        return HttpResponse(template.render()) 
def about(request):
        template = loader.get_template('about.html')
        return HttpResponse(template.render()) 
def report(request):
        template = loader.get_template('repo.html')
        return HttpResponse(template.render()) 
def login(request):
        error_message=None
        if request.POST: 
                username=request.POST['username']   
                password=request.POST['password'] 
                user=authenticate(username=username,password=password)
                if user:
                   authlogin(request,user)
                   return redirect('list')
                else :
                   error_message='invalid credentials'     
        return render(request,'logg.html')  
def logout(request):
        authlogout(request)
        return redirect('login')        
def register(request):
        error_message=None
        if request.POST:
                 name=request.POST['name']   
                 idno=request.POST['idno']   
                 email=request.POST['email']  
                 username=request.POST['username']   
                 password=request.POST['password'] 
                 try:
                         user=User.objects.create_user(name=name,idno=idno,email=email,username=username,password=password)      
                 except Exception as e:
                         error_message=str(e)
        return render(request,'register.html')        
def list(request):
        template = loader.get_template('list.html')
        return HttpResponse(template.render())             
def mngbook(request):
        template = loader.get_template('mngbook.html')
        return HttpResponse(template.render())   
def mngmem(request):
        dict_reader={
                'reader':Reader.objects.all()
        }
        template = loader.get_template('mngmem.html')
        return render(request, 'mngmem.html',dict_reader)
       # return HttpResponse(template.render())   
def profile(request):
        template = loader.get_template('profilefa.html')
        return HttpResponse(template.render())   
def profilesett(request):
        template = loader.get_template('profilesett.html')
        return HttpResponse(template.render())   