from django.template import loader
from django.contrib.auth import authenticate, login as authlogin, logout as authlogout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Reader
from .models import Book
from . import forms
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Customer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Book
from .forms import BookSearchForm
from .models import LibraryItem

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
       # name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('list')
        else:
            print("Inside error block")
            messages.error(request,'Invalid credentials.')
    return render(request,"login.html")
def AdminLogin(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('mngbook')
        else:
            print("Inside error block")
            messages.error(request,'Invalid credentials.')
    return render(request,"adminlogin.html")
 
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
                    name = name,
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

@login_required
def listBook(request):
        dict_books={
             'books':Book.objects.all()
         }
        #books=Book.objects.all()
        return render(request,'list.html',dict_books )            
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
@login_required  
def profile(request):
    return render(request, 'profilefa.html')
#def profile(request):
 #       template = loader.get_template('profilefa.html')
  #      return HttpResponse(template.render())   
def profilesett(request):
        template = loader.get_template('profilesett.html')
        return HttpResponse(template.render())   
def search_book(request):
   query = request.GET.get('query')
   results = []
   if query:
        results = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
   return render(request, 'search_book.html', {'query': query, 'results': results})

#fine calculations
def item(request):
        fine = item.calculate_fine()
        print("Fine for {item.title}: {fine} rupees")