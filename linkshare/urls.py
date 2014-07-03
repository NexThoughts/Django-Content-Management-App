from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth import views
urlpatterns = [
    # Examples:
    url(r'^$', 'linkshare.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^accounts/register/$', 'signup.views.register'),
    url(r'^accounts/register/$', 'signup.views.register_check'),
    url(r'^accounts/register_success/$', 'signup.views.register_success'),
    url(r'^accounts/login/$', 'signin.views.login'),
    url(r'^accounts/login_chk/$', 'signin.views.login_chk'),
    url(r'^accounts/invalid/$', 'signin.views.invalid_login'),
    url(r'^home/$', 'signin.views.home'),
    url(r'^resetpassword/passwordsent/$', 'django.contrib.auth.views.password_reset_done'),
    #url(r'^resetpassword/$', 'django.contrib.auth.views.password_reset'),
    #url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete'),
    #url(r'^user/pass/$', 'signup.views.pform'),
    url(r'^password_reset/$', views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', views.password_reset_complete, name='password_reset_complete'),
]
