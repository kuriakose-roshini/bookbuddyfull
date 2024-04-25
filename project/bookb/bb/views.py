from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
        template = loader.get_template('index.html')
        return HttpResponse(template.render()) 
def about(request):
        template = loader.get_template('about.html')
        return HttpResponse(template.render()) 
def report(request):
        template = loader.get_template('repo.html')
        return HttpResponse(template.render()) 
def login(request):
        template = loader.get_template('logg.html')
        return HttpResponse(template.render())         
def register(request):
        template = loader.get_template('register.html')
        return HttpResponse(template.render())        