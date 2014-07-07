from django.shortcuts import render,render_to_response
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from forms import LoginForm

# Create your views here.



def login_chk(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home/')
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username','')
            password = request.POST.get('password','')
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/home')
            else:
                return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
        else:
            return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
    else:
        form = LoginForm()
        context = {'form': form}
        return render_to_response('login.html', context, context_instance=RequestContext(request))

def LogoutRequest(request):
        logout(request)
        return HttpResponseRedirect('/')
