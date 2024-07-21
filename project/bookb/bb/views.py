from django.template import loader
from django.contrib.auth import authenticate, login as authlogin, logout as authlogout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import Reader
from .models import Book
from . import forms
from django.urls import reverse
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Customer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Borrower
#from .models import Invoice, is_due_date_approaching
from .forms import BookSearchForm
from django.http import JsonResponse
from .models import LibraryItem
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.utils import timezone

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

def loggot(request):
        authlogout(request)
        return redirect('index')
def Register(request):
 
    try:
        if request.POST:
            name = request.POST.get('name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')


            user = User.objects.create_user(
                    #name = name,
                    username = username,
                    password = password,
                    email = email,
                )
            
            customer = Customer.objects.create(
                    user = user,
                    name = name,
                   
                )


      
            
            return redirect('login')
            
    except IntegrityError as e:
        print(f"IntegrityError: {e}")
        error_message = "Duplicate username or invalid input data"
        print(error_message)
        messages.error(request,error_message)

      
    print("inside register")
    return render(request,'register.html')

@login_required
# def listBook(request):
      
#         books=Book.objects.all()
#         return render(request,'list.html',{'books':books})            
# def mngbook(request):
#         template = loader.get_template('mngbook.html')
#         books = Book.objects.all()
#         return HttpResponse(template.render(request, {'books': books}))  
#         books = Book.objects.all()
#         try:
#                 if request.POST and "ADD" in request.POST:
#                         Title= request.POST.get('Title')
#                         Name_of_Author= request.POST.get('Name_of_Author')
#                         Publisher = request.POST.get('Publisher')
#                         Arrival_date = request.POST.get('Arrival_date')
#                         No_Of_Copies_Available=request.POST.get('No_Of_Copies_Available')
#                         print(Title)
#                         print(Name_of_Author)
#                         print(Publisher)
#                         print(Arrival_date)
#                         print(No_Of_Copies_Available)

#                         books = Book.objects.create_book(
#                                 Title=Title,
#                                 Name_of_Author=Name_of_Author,
#                                 Publisher=Publisher,
#                                 Arrival_date=Arrival_date ,# Use first_name instead of name
#                         )              
                                  
#         except IntegrityError as e:
#                 print(f"IntegrityError: {e}")
#                 error_message = "invalid input data"
#                 print(error_message)
#                 messages.error(request,error_message)
#         return render(request, 'mngmem.html',{'books':books})
def mngbook(request):
    # Example: Fetching all books from the database
    books = Book.objects.all()
    try:
         if request.POST and "ADD" in request.POST:
                        Title = request.POST.get('Title')
                        Name_of_Author = request.POST.get('Name_of_Author')
                        Publisher = request.POST.get('Publisher')
                        Arrival_date = request.POST.get('Arrival_date')
                        No_of_Copies_Available = request.POST.get('No_of_Copies_Available')
                        print(Title)
                        print(Name_of_Author)
                        print(Publisher)
                        print(Arrival_date)
                        print(No_of_Copies_Available)

                        books = Book.objects.create(
                             Title=Title,
                             Name_of_Author=Name_of_Author,
                             Publisher=Publisher,
                             Arrival_date=Arrival_date,
                        )   
                  
    except IntegrityError as e:
                print(f"IntegrityError: {e}")
                error_message = "invalid input data"
                print(error_message)
                messages.error(request,error_message)
    
    
    # Prepare context dictionary to pass to the template
    context = {
        'books': books,
    }
    
    # Render the template with context data
    return render(request, 'mngbook.html', context)


def mngmem(request):
        reader = Customer.objects.all()
        try:
                if request.POST and "ADD" in request.POST:
                        name = request.POST.get('name')
                        username = request.POST.get('username')
                        email = request.POST.get('email')
                        password = request.POST.get('password')
                        print(name)
                        print(username)
                        print(email)

                        user = User.objects.create_user(
                                username=username,
                                email=email,
                                password=password,
                                first_name=name  
                        )              
                        customer = Customer.objects.create(
                                user = user,
                                name = name,
                               
                                )           
        except IntegrityError as e:
                print(f"IntegrityError: {e}")
                error_message = "Duplicate username or invalid input data"
                print(error_message)
                messages.error(request,error_message)
        return render(request, 'mngmem.html',{'reader':reader})
    
def borrow(request):
      template = loader.get_template('borrowerdisp.html')
      return HttpResponse(template.render())     
       
#@login_required  
#def profile(request):
 #   return render(request, 'profilefa.html')


@login_required
def profile(request):
    customer = request.user.customer_profile
    borrowed_books = Borrower.objects.filter(b_idnumber=customer)
    #fines = {borrower.id: borrower.calculate_fine() for borrower in borrowed_books}
    fines = {}
    total_fine = 0
    for book in borrowed_books:
        fine = book.calculate_fine()
        fines[book.id] = fine
        total_fine += fine

    return render(request, 'profilefa.html', {
        'borrowed_books': borrowed_books,
        'fines': fines,
        'total_fine': total_fine,
    })

#@login_required
#def profile(request):
 #   borrowed_books = Borrower.objects.filter(b_idnumber=request.user.customer_profile)
  #  return render(request, 'profile.html', {'borrowed_books': borrowed_books})
 
def profilesett(request):
        template = loader.get_template('profilesett.html')
        return HttpResponse(template.render())   


# #message notification
# def send_due_date_notification(request):
#     invoices = Invoice.objects.all()
#     for invoice in invoices:
#         if is_due_date_approaching(invoice):
#             notification_message = "Your invoice with due date {invoice.due_date} is approaching. Please make sure to pay on time."
#             messages.info(request, notification_message)
#     return render(request, 'notification_sent.html')


#logout
# views.py
from django.contrib.auth import logout
from django.shortcuts import redirect
def logout_view(request):
     logout(request)
     return redirect(reverse('login'))
     #response = redirect('login')  # Redirect to your login page
     #response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
     #response['Pragma'] = 'no-cache'
     #response['Expires'] = '0'
     #return response
        
#fine calc
from django.shortcuts import render, redirect
from .models import BorrowedBook

def return_book(request, borrowed_book_id):
    borrowed_book =get_object_or_404(Borrower, id=borrowed_book_id)
    fine = borrowed_book.calculate_fine()
    # You can add the fine to the user's account or display it on the return page
    return render(request, 'return_book.html', {'fine': fine})

#search book
from django.shortcuts import render
from .models import Book
#for index
def search_books(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(Title__icontains=query)
    else:
        books = []
    return render(request, 'index.html',{'books': books})

#for list
def search_books_list(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(Title__icontains=query)
    else:
        books = []
    return render(request, 'list.html',{'books': books})

# def request_book(request, book_id):
#     if request.method == 'POST':
#         book = get_object_or_404(Book, id=book_id)
#         reader = get_object_or_404(Reader, user=request.user)  # Assuming the Reader is related to the current user

#         borrower = Borrower.objects.create(
#             b_name=request.user.get_full_name(),
#             b_idnumber=reader,
#             b_emailid=request.user.email,
#             b_username=request.user.username,
#             b_date_of_borrow=timezone.now(),
#             b_return_date=timezone.now() + timezone.timedelta(days=14)  # Example: 14 days borrowing period
#         )
#         return redirect('list_books')  # Redirect to the list of books or any other page

#     return HttpResponse(status=405)

#def borrowers(request):
 #     borrowers = Borrower.objects.all()
  #    return render(request, 'borrowerdisp.html', {'borrower': borrowers})


def listBook(request):
   books = Book.objects.all()
   return render(request, 'list.html', {'books': books})

def request_book(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, id=book_id)
        print(f"Current user: {request.user.username}")  # Debugging print statement

        try:
            customer = request.user.customer_profile
            print(f"Customer found: {customer.name}")
        except Customer.DoesNotExist:
            print("No matching Customer found")
            return HttpResponse("No matching Customer found", status=404)
        
        borrowed_books_count = Borrower.objects.filter(b_idnumber=customer).count()
        if borrowed_books_count >= 3:
            messages.error(request, "You cannot borrow more than 3 books at a time.")
            return redirect('list')

        borrower=Borrower.objects.create(
            b_name=customer.name,
            b_idnumber=customer,  # Assuming Borrower model can reference Customer model
            b_emailid=request.user.email,
            b_username=request.user.username,
            b_date_of_borrow=timezone.now(),
            b_return_date=timezone.now() + timezone.timedelta(days=14), # Example: 14 days borrowing period
            b_bookid=book
        )
        messages.success(request, "Book requested successfully")
        return redirect('list')

    return HttpResponse(status=405)

def borrowers(request):
      borrowers = Borrower.objects.all()
      return render(request,'borrowerdisp.html',{'borrowers': borrowers})

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def delete_borrower(request, borrower_id):
    if request.method == 'DELETE':
        borrower = get_object_or_404(Borrower, id=borrower_id)
        borrower.delete()
        
        # Reset IDs after deletion
        borrowers = Borrower.objects.all().order_by('id')
        for index, borrower in enumerate(borrowers):
            borrower.id = index + 1
            borrower.save()
        
        return JsonResponse({'message': 'Borrower deleted and IDs reset successfully.'}, status=200)
    return JsonResponse({'error': 'Invalid request method.'}, status=405)


def delete_book(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, id=book_id)
        book.delete()
        reset_book_ids()  # Call the function to reset IDs
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

def reset_book_ids():
    books = Book.objects.all().order_by('id')
    for index, book in enumerate(books, start=1):
        book.id = index
        book.save()


#import json
#@csrf_exempt
#def add_book(request):
#    if request.method == 'POST':
#        data = json.loads(request.body)
 #       book = Book.objects.create(
  #          Title=data.get('Title'),
   #         Name_of_Author=data.get('Name_of_Author'),
    #        Publisher=data.get('Publisher'),
     #       Arrival_date=data.get('Arrival_date'),
      #      No_Of_Copies_Available=data.get('No_Of_Copies_Available')
       # )
      #  return JsonResponse({'success': True, 'id': book.id})
    #return JsonResponse({'success': False})


@csrf_exempt
def delete_member(request, member_id):
    if request.method == 'DELETE':
        member = get_object_or_404(Customer, id=member_id)
        member.delete()
        
        # Reset IDs after deletion
        reset_member_ids()
        
        return JsonResponse({'message': 'Member deleted.'}, status=200)
    return JsonResponse({'error': 'Invalid request method.'}, status=405)

from django.db import transaction
@transaction.atomic
def reset_member_ids():
    members = Customer.objects.all().order_by('id')
    for index, member in enumerate(members, start=1):
        member.id = index
        member.save()