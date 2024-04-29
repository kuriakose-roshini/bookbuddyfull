from django.template import loader
from django.contrib.auth import authenticate, login as authlogin, logout as authlogout
from django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Reader 
from . import forms
from django.db import IntegrityError
from django.contrib import messages




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
#def register(request):
 #       template = loader.get_template('register.html')
 #       return HttpResponse(template.render())    
#def register(request):
    #context = context_data(request)
    #context['topbar'] = False
    #context['footer'] = False
    #context['page_title'] = "User Registration"
   # if request.user.is_authenticated:
    #    return redirect('register')
    #return render(request, 'login')
#def register(request):
                 
        #error_message=None
        #if request.method == 'POST':
                 #Name = request.POST.get('Name')   
                 #idno = request.POST.get('idno') 
                 #emailid = request.POST.get('emailid') 
                 #u_name = request.POST.get('u_name')  
                 #pwd1 = request.POST.get('pwd1') 
                 #pwd2 = request.Post('pwd2')
                 #try:
                 ##reader_obj = Reader.objects.create(Name=Name,idno=idno,emailid=emailid,u_name=u_name,pwd=pwd1)      
                 #except Exception as e:
                  #error_message=str(e)
                #form = RegisterForm(response.POST)
                #if form.is_valid():
                 #reader_obj.save()
                 #print("user created")
                 #if request.user.is_authenticated:
                 # return redirect( 'login')
                #else:
        #else :              
       # return render(request,'register.html')      

def register(request):
 
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
        
            #role = request.POST.get('options')

            reader = Reader.objects.create(
                    user = user,
                    name = name,
                    email = email
                )
            
        #if(role=='teacher'):
             #   return redirect("home")
            #else:
        return redirect("login")
            
    except IntegrityError as e:
        print(f"IntegrityError: {e}")
        error_message = "Duplicate username or invalid input data"
        print(error_message)
        messages.error(request,error_message)

       

    return render(request,'register.html')


#def Login(request):
  #  if request.POST:
   #     username = request.POST.get('username')
    #    password = request.POST.get('password')
     #   user = authenticate(username=username,password=password)
      #  if user:
#            login(request,user)
 #    return redirect('home1')
  #      else:
   #         print("Inside error block")
    #        messages.error(request,'Invalid credentials.')
    #return render(request,"login.html")  
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
def search_book(request):
    if request.method == 'GET':
        input_query = request.GET.get('searchbar', '').lower()
        books = Book.objects.filter(title__icontains=input_query)  # Assuming 'title' is the field to search
        return render(request, 'search_results.html', {'books': books})
        #if request.method =='GET':
                #search=request.GET.get('search')
                #post=bb.objects.all().filter(title=search)
                #return render(request,'searchbar.html',{'post':post})