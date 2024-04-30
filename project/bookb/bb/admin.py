from django.contrib import admin
from .models import Reader,Borrower,Book,LibraryItem,Profile

# Register your models here.
admin.site. register(Reader)
admin.site. register(Borrower)
admin.site. register(Book)
admin.site. register(LibraryItem)
admin.site. register(Profile)

