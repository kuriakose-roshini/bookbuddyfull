from django.template import loader
from django.contrib.auth import authenticate, login as authlogin, logout as authlogout
from django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Reader
#from.models import Book
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
        if request.method == 'POST':
                 name=request.POST['Name']   
                 idno=request.POST['idno'] 
                 emailid=request.POST['emailid']  
                 username=request.POST['u_name']   
                 password1=request.POST['pwd1'] 
                 password2=request.Post['pwd2']
                 try:
                  user=User.objects.create_user(name=name,idno=idno,email=emailid,username=username,password=password1)      
                 except Exception as e:
                  error_message=str(e)
                #form = RegisterForm(response.POST)
                #if form.is_valid():
                 user.save()
                 print("user created")
                 return redirect(' login ')
                #else:
        else :              
                return render(request,'register.html')   
@login_required(login_url='login/')             
def list(request):
        dict_book={
               'book':Book.objects.all()
        }
        template = loader.get_template('list.html')
        return render(request,'list.html',dict_book)
        #return HttpResponse(template.render())             
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
def search_book(request):
    if request.method == 'GET':
        input_query = request.GET.get('searchbar', '').lower()
        books = Book.objects.filter(title__icontains=input_query)  # Assuming 'title' is the field to search
        return render(request, 'search_results.html', {'books': books})
        #if request.method =='GET':
                #search=request.GET.get('search')
                #post=bb.objects.all().filter(title=search)
                #return render(request,'searchbar.html',{'post':post})