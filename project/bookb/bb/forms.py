from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BookSearchForm(forms.Form):
  query = forms.CharField(label='Search')
#class RegisterForm(UserCreationForm):
#name = forms .CharField(max_length=50,required=False)

  #  class Meta:
    #    model = User
     #   fields = ["name","idno","emailid","u_name","pwd1","pwd2"]