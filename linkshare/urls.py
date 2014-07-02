from django.conf.urls import include, url
from django.contrib import admin

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
    url(r'^user/password/reset/$',
        'django.contrib.auth.views.password_reset',
        {'post_reset_redirect' : '/user/password/reset/done/'},
        name="password_reset"),
    url(r'^user/password/reset/done/$',
        'django.contrib.auth.views.password_reset_done'),
    url(r'^user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'post_reset_redirect' : '/user/password/done/'}),
    url(r'^user/password/done/$',
        'django.contrib.auth.views.password_reset_complete'),
    url(r'^user/pass/$', 'signup.views.pform'),
]
