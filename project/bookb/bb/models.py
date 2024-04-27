from django.db import models

# Create your models here.
class Reader(models.Model):
    name=models.CharField(max_length=20,blank=False,null=False)
    idnumber=models.CharField(max_length=25,blank=False,null=False)
    emailid=models.EmailField(null=True)
    username=models.CharField(max_length=30,null=True)
    password=models.CharField(max_length=8,blank=False,null=False)

    class Meta:
        verbose_name_plural = "List of Readers"
    
    def __str__(self) :
        return self.name

    
    #def __str__(self):
     #   return str(f"{self.id} - {self.first_name}{' '+self.middle_name if not self.middle_name == '' else ''} {self.last_name}")

    #def name(self):
     #   return str(f"{self.first_name}{' '+self.middle_name if not self.middle_name == '' else ''} {self.last_name}")

    

