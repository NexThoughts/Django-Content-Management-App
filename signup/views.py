from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from forms import Signup, Confirm
# Create your views here.
def register(request):
    if request.method == "POST":
        form = Signup(request.POST)
        if form.is_valid():
            form.save()


    args = {}
    args.update(csrf(request))

    args['form']=Signup()
    print args
    return render_to_response('register.html', args)