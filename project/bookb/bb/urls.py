from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('report/', views.report, name="report"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('listbook/', views.list, name="list"),
    path('managebook/', views.mngbook, name="mngbook"),
    path('managemembers/', views.mngmem, name="mangmem"),
]