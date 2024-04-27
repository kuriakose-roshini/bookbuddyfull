from django.db import models

# Create your models here.
class Reader(models.Model):
    name=models.CharField(max_length=20,blank=False,null=True)
    idnumber=models.CharField(max_length=25,blank=False,null=False)
    emailid=models.EmailField(null=True)
    username=models.CharField(max_length=30,null=True)
    password=models.CharField(max_length=8,blank=False,null=False)

    class Meta:
        verbose_name_plural = "List of Readers"
    
    def __str__(self) :
        return self.username

    
    #def __str__(self):
     #   return str(f"{self.id} - {self.first_name}{' '+self.middle_name if not self.middle_name == '' else ''} {self.last_name}")

    #def name(self):
     #   return str(f"{self.first_name}{' '+self.middle_name if not self.middle_name == '' else ''} {self.last_name}")

    #class Books(models.Model):
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

    

