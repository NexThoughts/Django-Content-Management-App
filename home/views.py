from django.shortcuts import render,render_to_response
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
# Create your views here.
def not_in_student_group(user):
    if user:
        return user.groups.filter(name='Django').count() == 0
    return False

@login_required
@user_passes_test(not_in_student_group, login_url='/accounts/register/')
def homepage(request):
    if request.user.is_authenticated():
        return render_to_response('home.html')
    return HttpResponseRedirect('/accounts/login')
