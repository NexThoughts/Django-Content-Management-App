from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
urlpatterns = [
    # Examples:
    url(r'^$', 'linkshare.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^accounts/register/$', 'signup.views.register'),
    #url()
    url(r'^accounts/register/$', 'signup.views.register_check'),
    url(r'^accounts/register_success/$', 'signup.views.register_success'),

    url(r'^accounts/login/$', 'signin.views.login_chk'),
    url(r'^accounts/logout/$', 'signin.views.LogoutRequest'),
    url(r'^accounts/login_chk/$', 'signin.views.login_chk'),
    url(r'^password_reset/$', 'signup.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', views.password_reset_complete, name='password_reset_complete'),

    url(r'^home/$', 'home.views.homepage'),
    url(r'^logout/$', 'signin.views.LogoutRequest'),

    url(r'^article/add/','article.views.UploadArticle'),
    url(r'^articles/all/','article.views.articles'),
    url(r'^articles/get/(?P<article_id>\d+)/$', 'article.views.article'),
    url(r'^view/group/$', 'home.views.grp'),
    url(r'^view/group/all','home.views.groupall'),
    url(r'^view/get/(?P<join>[0-9A-Za-z_\-]+)/$',
        'home.views.GetGroup'),

]
