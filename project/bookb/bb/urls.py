from django.contrib import admin
from django.urls import include,path
from . import views
from .views import profile
from django.urls import path
from .views import index, search_books, search_books_list

urlpatterns = [
    path('', views.index, name="index"),
    
    path('about/', views.about, name="about"),
    path('register/', views.Register, name="user"),
    path('report/', views.report, name="report"),
    path('login/', views.Login, name="login"),
    path('logout/', views.loggot, name="Logout"),
    path('adminlogin/', views.AdminLogin, name="adminlogin"),
    path('logout/', views.logout_view, name="logout"),
    #path('searchbook/', views.search_book, name="search_book"),
    path('listbook/', views.listBook, name="list"),
    path('managebook/', views.mngbook, name="mngbook"),
    path('managemembers/', views.mngmem, name="mngmem"),
    #path('borrowers/', views.borrow, name="borrow"),
    path('borrowers/',views.borrowers,name="borrowers"),
    path('profile/', views.profile, name="profilefa"),
    path('profile:settings/', views.profilesett, name="profilesett"),
    #path('books/',views.listBook,name='listBook'),
    path('search/', search_books, name='search_books'),
    path('searchbooks/', search_books_list, name='search_books_list'),
    path('request_book/<int:book_id>/', views.request_book, name='request_book'),
    path('delete_borrower/<int:borrower_id>/', views.delete_borrower, name='delete_borrower'),
    #path('add_book/', views.add_book, name='add_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    
    ]