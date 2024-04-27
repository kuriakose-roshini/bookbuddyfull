from django.template import loader
from . import forms
from django.contrib import messages
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse


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
        pass
def register(request):

       # if request.method=="POST": 
        #        name=request.POST.get('Name')
         #       idnumber=request.POST.get('id')
          #      username=request.POST.get('emailid')
           #     password=request.POST.get('pwd')
            #    print(name,username,idnumber,password)
             #  query=Reader(name=Name,idnumber=id,username=emailid,password=pwd)
              #  query.save()
        context = context_data(request)
        context['topbar'] = False
        context['footer'] = False
        context['page_title'] = "Registration"
        if request.user.is_authenticated:
           return redirect("list")
        return render(request, 'register.html', context)
        """
        resp={'status':'failed', 'msg':''}
        if not request.method == 'POST':
                resp['msg'] = "No data has been sent on this request"
        else:
                form = forms.SaveUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Account has been created succesfully")
            resp['status'] = 'success'
        else:
            for field in form:
                for error in field.errors:
                    if resp['msg'] != '':
                        resp['msg'] += str('<br />')
                        resp['msg'] += str(f"[{field.name}] {error}.")
            
        return HttpResponse(json.dumps(resp), content_type="application/json")"""
def list(request):
        template = loader.get_template('list.html')
        return HttpResponse(template.render())     
def context_data(request):
    fullpath = request.get_full_path()
    abs_uri = request.build_absolute_uri()
    abs_uri = abs_uri.split(fullpath)[0]
    context = {
        'system_host' : abs_uri,
        'page_name' : '',
        'page_title' : '',
        'system_name' : 'Library Managament System',
        'topbar' : True,
        'footer' : True,
    }
    return context
        
def mngbook(request):
        template = loader.get_template('mngbook.html')
        return HttpResponse(template.render())   
def mngmem(request):
        template = loader.get_template('mngmem.html')
        return HttpResponse(template.render())   