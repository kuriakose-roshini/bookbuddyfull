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

# Create your models here.
class Reader(models.Model):
    name=models.CharField(max_length=20,blank=False,null=True)
    idnumber=models.CharField(max_length=25,blank=False,null=False)
    emailid=models.EmailField(null=True)
    username=models.CharField(max_length=30,null=True)
    password=models.CharField(max_length=8,blank=False,null=False)



class Book(models.Model):
    No=models.CharField(max_length=30)
    Title=models.CharField(max_length=200) 
    Name_of_Author=models.CharField(max_length=200)
    Publisher=models.CharField(max_length=250)
    Arrival_date=models.DateField()
    No_Of_copies_Available=models.CharField(max_length=30,null=False)
     

     
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
class Borrower(models.Model):
    b_name=models.CharField(max_length=20,blank=False,null=True)
    b_idnumber=models.ForeignKey(Reader, on_delete=models.CASCADE)
    b_emailid=models.EmailField(null=True)
    b_username=models.CharField(max_length=30,null=True)
    b_date_of_borrow=models.DateField()
    b_return_date=models.DateField()

    def __str__(self):
        return self.b_username

class Customer(models.Model):

    LIVE = 0
    DELETE = 0
    DELETE_CHOICES = ((LIVE,'Live'),(DELETE,'Delete'))

    name = models.CharField(max_length=100,null=False,blank=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='customer_profile')
 



    deleted_status = models.IntegerField(choices=DELETE_CHOICES ,default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)    

