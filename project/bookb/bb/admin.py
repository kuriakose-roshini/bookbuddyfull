from django.contrib import admin
from .models import Reader,Borrower,Book

# Register your models here.
admin.site. register(Reader)
admin.site. register(Borrower)
admin.site. register(Book)
