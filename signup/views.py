from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from forms import Signup
from django.template import RequestContext
from django.contrib.auth import views
from django.core.mail import send_mail
from django.core.mail.backends import smtp
# Create your views here.
def register_check(request):
    if request.method == "POST":
        form = Signup(request.POST)
        if form.is_valid():
            form.save()
            send_mail('Noreply', 'content' , 'abhilashjha@gmail.com', ['abhilashjha@gmail.com'], fail_silently=False)
            return HttpResponseRedirect('/accounts/register_success')
        else:
            return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))

    args = {}
    args.update(csrf(request))

    args['form']=Signup()
    print args
    return render_to_response('register.html', args)

def register_success(request):
    return render_to_response('register_success.html')


