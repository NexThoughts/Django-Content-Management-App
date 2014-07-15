from django.shortcuts import render, render_to_response
from forms import AddArticle
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from article.models import Article
from django.contrib.auth.models import User,Group
from django.contrib.auth.decorators import login_required
# Create your views here.
def UploadArticle(request, grp):
    if request.POST:
        form = AddArticle(request.POST)
        if form.is_valid():
            check=form.save(commit=False)
            check.Author_id = request.user
            check.group_id = Group.objects.get(name=grp)
            check.save()
            return HttpResponseRedirect('/articles/all')
        else:
            form = AddArticle()

    args = {}
    args.update(csrf(request))
    args['form']=AddArticle()
    return render_to_response('add.html', args)

def article(request, article_id=1):
    return render_to_response('view.html',{'article': Article.objects.get(id=article_id)})

def articles(request, grp):
    return render_to_response('articles.html', { 'articles' : Article.objects.all(), 'grp':grp })

@login_required()
def ShowGroup(request, grp, article_id=1):
    parameter = request.user.id
    g=Group.objects.get(name=grp).id
    return render_to_response('MyGroup.html', {'parameter': parameter, 'articles': Article.objects.all(), 'grp':g })