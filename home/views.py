from django.shortcuts import render,render_to_response
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User,Group
from article.models import Article
# Create your views here.

@login_required
def homepage(request):
    if request.user.is_authenticated():
        c=request.user.groups.all()
        u=request.user
        n=Group.objects.exclude(id__in=request.user.groups.all().values_list('id', flat=True))
        r=Article.objects.filter(Author_id_id=u.id)
        return render_to_response('home.html',{'check' : c , 'user': u, 'nongrp': n, 'articles': Article.objects.order_by('art_date').reverse()[:5], 'num': r })
    return HttpResponseRedirect('/accounts/login')
@login_required
def grp(request):
    l=request.user.groups.all().values_list('name', flat=True)
    u=request.user
    n=Group.objects.exclude(id__in=request.user.groups.all().values_list('id', flat=True))

    r=Article.objects.filter(Author_id_id=u.id)
    return render_to_response('group.html',{'check' : l , 'user': u, 'check2': n, 'nongrp': n.reverse()[:8], 'num':r })
@login_required
def GetGroup(request, join):
    g = Group.objects.get(name=join)
    user=request.user
    g.user_set.add(user)
    return HttpResponseRedirect("/view/group/"+join)
@login_required
def DeleteGroup(request, grp):
    g= Group.objects.get(name=grp)
    user=request.user
    g.user_set.remove(user)
    return HttpResponseRedirect("/view/group")