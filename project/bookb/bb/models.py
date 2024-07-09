from django.db import models
#from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

#from PIL import Image
from django.contrib.auth.models import User
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone
from django.db import models
from django.utils import timezone

# Create your models here.
# class Reader(models.Model):
#     name=models.CharField(max_length=20,blank=False,null=True)
#     idnumber=models.CharField(max_length=25,blank=False,null=False)
#     emailid=models.EmailField(null=True)
#     username=models.CharField(max_length=30,null=True)
#     password=models.CharField(max_length=8,blank=False,null=False)

class Reader(models.Model):
    name = models.CharField(max_length=20, blank=False, null=True)
    idnumber = models.CharField(max_length=25, blank=False, null=False)
    emailid = models.EmailField(null=True)
    username = models.CharField(max_length=30, null=True)
    password = models.CharField(max_length=8, blank=False, null=False)

    def _str_(self):
        return self.username



class Book(models.Model):
   # No=models.CharField(max_length=30)
    Title=models.CharField(max_length=200) 
    Name_of_Author=models.CharField(max_length=200)
    Publisher=models.CharField(max_length=250)
    Arrival_date=models.DateField()  
    No_Of_copies_Available=models.CharField(max_length=30,null=False)
       
    def __str__(self):
           return self.Title
     # models.py


# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     Name_of_Author = models.CharField(max_length=200)
#     Publisher=models.CharField(max_length=250)
#     No_Of_copies_Available=models.CharField(max_length=30,null=False)
#     #description = models.TextField()
#     #published_date = models.DateField()

#     def _str_(self):
#         return self.title

     
    #class Meta:
       # verbose_name_plural = "List of Readers"
    
  #  def __str__(self) :
    #  return self.username

    
    #def __str__(self):
     #   return str(f"{self.id} - {self.first_name}{' '+self.middle_name if not self.middle_name == '' else ''} {self.last_name}")

    #def name(self):
     #   return str(f"{self.first_name}{' '+self.middle_name if not self.middle_name == '' else ''} {self.last_name}")

   # class Books(models.Model):
    # no= models.IntegerField(max_length=10,blank=False,null=False)
     #name_of_book= models.CharField(max_length=30,blank=False,null=False)
   # borrowing_date = models.DateField()
    #return_date = models.DateField()
    #status = models.CharField(max_length=2, choices=(('1','Pending'), ('2','Returned')), default = 1)
    #date_added = models.DateTimeField(default = timezone.now)
    #date_created = models.DateTimeField(auto_now = True)

    #class Meta:
     #   verbose_name_plural = "List of books"

    #def __str__(self):
     #   return self.name_of_book

# class Borrower(models.Model):
#     b_name=models.CharField(max_length=20,blank=False,null=True)
#     b_idnumber=models.ForeignKey(Reader, on_delete=models.CASCADE)
#     b_emailid=models.EmailField(null=True)
#     b_username=models.CharField(max_length=30,null=True)
#     b_date_of_borrow=models.DateField()
#     b_return_date=models.DateField()

#     def __str__(self):
#         return self.b_username



class Customer(models.Model):

    LIVE = 0
    DELETE = 0
    DELETE_CHOICES = ((LIVE,'Live'),(DELETE,'Delete'))

    name = models.CharField(max_length=100,null=False,blank=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='customer_profile')
 



    deleted_status = models.IntegerField(choices=DELETE_CHOICES ,default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)    
    def __str__(self):
        return self.name
    

class Borrower(models.Model):
    b_name = models.CharField(max_length=20, blank=False, null=True)
    b_idnumber = models.ForeignKey(Customer, on_delete=models.CASCADE)  # Reference Customer model
    b_emailid = models.EmailField(null=True)
    b_username = models.CharField(max_length=30, null=True)
    b_date_of_borrow = models.DateField()
    b_return_date = models.DateField()
   # b_title =models.CharField(max_length=200)
    b_title = models.ForeignKey(Book, on_delete=models.CASCADE,default=1)
    #b_title=models.ForeignKey(Book, on_delete=models.CASCADE,default=1) 

    def _str_(self):
        return self.b_username
    
#profile
class Profile(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)
    user = models.OneToOneField(Customer, on_delete=models.CASCADE)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.user.name


  #fine calculations
class LibraryItem(models.Model):
    title = models.CharField(max_length=100)
    #Name_of_Author=models.CharField(max_length=200)
    #Publisher=models.CharField(max_length=250)
    #Arrival_date=models.DateField()  
    #No_Of_copies_Available=models.CharField(max_length=30,null=False)
    due_date = models.DateField()

    def calculate_fine(self):
        overdue_days = (timezone.now().date() - self.due_date).days
        if overdue_days > 14:
            fine_amount = overdue_days - 14  # Fine is 1 rupee per day after 14 days
        else:
            fine_amount = 0
        return fine_amount

#message notification
#lass Invoice(models.Model):
#   customer = models.ForeignKey(User, on_delete=models.CASCADE)
#   amount = models.DecimalField(max_digits=10, decimal_places=2)
#   due_date = models.DateField()
#   def is_due_date_approaching(invoice, days_threshold=7):
#      today = timezone.now().date()
#      return (invoice.due_date - today).days <= days_threshold
#


#fine calc


class BorrowedBook(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateField(default=timezone.now)
    due_date = models.DateField()

    @property
    def calculate_fine(self):
        if self.due_date < timezone.now().date():
            days_overdue = (timezone.now().date() - self.due_date).days
            fine = days_overdue * 0.50  # Example: $0.50 per day
            return fine
        else:
            return 0
