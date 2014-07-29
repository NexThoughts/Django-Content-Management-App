from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from forms import Signup
from django.template import RequestContext
from django.contrib.auth import views
from django.core.mail import send_mail
from django.core.mail.backends import smtp
from forms import PasswordResetForm
from django import forms


from django.core.urlresolvers import reverse
from django.template.response import TemplateResponse
from django.utils.translation import ugettext as _
from django.shortcuts import resolve_url
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth.tokens import default_token_generator



# Create your views here.
def register_check(request):
    if request.method == "POST":
        form = Signup(request.POST)
        if form.is_valid():
            form.save()
                        #send_mail('Noreply', 'content' , 'abhilashjha@gmail.com', ['abhilashjha@gmail.com'], fail_silently=False)
            return HttpResponseRedirect('/accounts/register_success')
        else:
            return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))

    #args = {}
    #args.update(csrf(request))
    #args['form']=Signup()
    #print args
    form = Signup()
    context = {'form': form}
    return render_to_response('register.html', context, context_instance=RequestContext(request))

def register_success(request):
    return render_to_response('register_success.html')

@csrf_protect
def password_reset(request, is_admin_site=False,
                   template_name='registration/password_reset_form.html',
                   email_template_name='registration/password_reset_email.html',
                   subject_template_name='registration/password_reset_subject.txt',
                   password_reset_form=PasswordResetForm,
                   token_generator=default_token_generator,
                   post_reset_redirect=None,
                   from_email=None,
                   current_app=None,
                   extra_context=None,
                   html_email_template_name=None):
    if post_reset_redirect is None:
        post_reset_redirect = reverse('password_reset_done')
    else:
        post_reset_redirect = resolve_url(post_reset_redirect)
    if request.method == "POST":
        form = password_reset_form(request.POST)
        if form.is_valid():
            opts = {
                'use_https': request.is_secure(),
                'token_generator': token_generator,
                'from_email': from_email,
                'email_template_name': email_template_name,
                'subject_template_name': subject_template_name,
                'request': request,
                'html_email_template_name': html_email_template_name,
            }
            if is_admin_site:
                opts = dict(opts, domain_override=request.get_host())
            form.save(**opts)
            return HttpResponseRedirect(post_reset_redirect)
    else:
        form = password_reset_form()
    context = {
        'form': form,
        'title': _('Password reset'),
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
                            current_app=current_app)


def password_reset_done(request,
                        template_name='registration/password_reset_done.html',
                        current_app=None, extra_context=None):
    context = {
        'title': _('Password reset successful'),
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
                            current_app=current_app)

