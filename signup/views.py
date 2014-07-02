from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from forms import Signup
from django.contrib.auth import views
# Create your views here.
def register_check(request):
    if request.method == "POST":
        form = Signup(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')

    args = {}
    args.update(csrf(request))

    args['form']=Signup()
    print args
    return render_to_response('register.html', args)

def register_success(request):
    return render_to_response('register_success.html')

def pform(request):
    args = {}
    args.update(csrf(request))
    print args
    return render_to_response('registration/password_reset_form.html', args)