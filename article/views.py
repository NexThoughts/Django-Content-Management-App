from django.shortcuts import render, render_to_response,get_object_or_404
from forms import AddArticle,AddComments
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from article.models import Article,Comments
from django.contrib.auth.models import User,Group
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import linebreaks_filter
# Create your views here.

@login_required
def UploadArticle(request, grp):
    if request.POST:
        form = AddArticle(request.POST, request.FILES)
        if form.is_valid():
            check=form.save(commit=False)
            check.Author_id = request.user
            check.group_id = Group.objects.get(name=grp)
            check.save()
            return HttpResponseRedirect('/view/group/'+grp)
        else:
            form = AddArticle()

    args = {}
    args.update(csrf(request))
    args['form']=AddArticle()
    args['user']=request.user
    args['nongrp']=Group.objects.exclude(id__in=request.user.groups.all().values_list('id', flat=True)).reverse()[:8]
    args['num']=Article.objects.filter(Author_id_id=request.user.id)
    return render_to_response('add.html', args)

@login_required
def article(request, grp, article_id=1):
    if request.POST:
        form = AddComments(request.POST)
        if form.is_valid():
            verify=form.save(commit=False)
            verify.User_id = request.user
            verify.Group_id = Group.objects.get(name=grp)
            verify.Article_id = Article.objects.get(id=article_id)
            verify.save()
            return HttpResponseRedirect('')
        else:
            form = AddComments()

    args = {}
    args.update(csrf(request))
    args['form']=AddComments()
    args['article']= Article.objects.get(id=article_id)
    args['comment']= Comments.objects.all()
    args['user']=request.user
    args['nongrp']=Group.objects.exclude(id__in=request.user.groups.all().values_list('id', flat=True))
    args['num']=Article.objects.filter(Author_id_id=request.user.id)
    return render_to_response('view.html', args)

@login_required
def articles(request, grp):
    return render_to_response('articles.html', { 'articles' : Article.objects.all(), 'grp':grp, 'user':request.user })

@login_required()
def ShowGroup(request, grp, article_id=1):
    parameter = request.user
    g=Group.objects.get(name=grp).id
    return render_to_response('MyGroup.html', {'parameter': parameter.id, 'articles': Article.objects.all(), 'grp':g ,'user':parameter,'num': Article.objects.filter(Author_id_id=request.user.id), 'nongrp' : Group.objects.exclude(id__in=request.user.groups.all().values_list('id', flat=True)).reverse()[:8] })

@login_required
def rem_art(request, art_id, grp):
    r=Article.objects.get(id=art_id)
    if request.user == r.Author_id:
        r.delete()
    return HttpResponseRedirect("/view/group/"+grp)

@login_required
def edit_article(request, grp, article_id):
    art=Article.objects.get(id=article_id)
    if request.user == art.Author_id:
        if request.POST:
            form = AddArticle(request.POST, request.FILES, instance=art)
            if form.is_valid():
                check=form.save(commit=False)
                check.Author_id = request.user
                check.group_id = Group.objects.get(name=grp)
                check.File = ''
                check.save()
                return HttpResponseRedirect('/home')
            else:
                form = AddArticle(instance=art)
        args = {}
        args.update(csrf(request))
        args['form']=AddArticle(instance=art)
        args['user']=request.user
        args['nongrp']=Group.objects.exclude(id__in=request.user.groups.all().values_list('id', flat=True)).reverse()[:8]
        args['num']=Article.objects.filter(Author_id_id=request.user.id)
        return render_to_response('edit.html', args)
    else:
        return HttpResponseRedirect('/home/')