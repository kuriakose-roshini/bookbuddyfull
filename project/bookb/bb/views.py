from django.template import loader
from django.contrib.auth import authenticate, login as authlogin, logout as authlogout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Reader
from . import forms
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Customer
from django.contrib.auth.decorators import login_required

#from .forms import RegisterForm




def index(request):
        template = loader.get_template('index.html')
        return HttpResponse(template.render()) 
def about(request):
        template = loader.get_template('about.html')
        return HttpResponse(template.render()) 
def report(request):
        template = loader.get_template('repo.html')
        return HttpResponse(template.render()) 
def Login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('register')
        else:
            print("Inside error block")
            messages.error(request,'Invalid credentials.')
    return render(request,"login.html")
 
def logout(request):
        authlogout(request)
        return redirect('login')     
      

def Register(request):
 
    try:
        if request.POST:
            name = request.POST.get('name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')


            user = User.objects.create_user(
                    username = username,
                    password = password,
                    email = email,
                )
        
           

            customer = Customer.objects.create(
                    user = user,
                    name = name,
                   
                )


      
            
            return redirect("list")
            
    except IntegrityError as e:
        print(f"IntegrityError: {e}")
        error_message = "Duplicate username or invalid input data"
        print(error_message)
        messages.error(request,error_message)

       
    print("inside register")
    return render(request,'register.html')

# @login_required
def listBook(request):
        return render(request,"list.html")            
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
# def search_book(request):
#     if request.method == 'GET':
#         input_query = request.GET.get('searchbar', '').lower()
#         books = Book.objects.filter(title__icontains=input_query)  # Assuming 'title' is the field to search
#         return render(request, 'search_results.html', {'books': books})
        #if request.method =='GET':
                #search=request.GET.get('search')
                #post=bb.objects.all().filter(title=search)
                #return render(request,'searchbar.html',{'post':post})