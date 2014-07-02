from django.shortcuts import render,render_to_response
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
# Create your views here.



def login_chk(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/home')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def home(request):
    return render_to_response('home.html')

def invalid_login(request):
    return render_to_response('invalid_login.html')

def login(request):
    c={}
    c.update(csrf(request))
    return render_to_response('login.html',c)
