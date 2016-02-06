from django.conf.urls import patterns, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from plucoApp import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'about',views.about,name='about'),
        url(r'contact',views.contact,name='contact'),
        url(r'register',views.register,name='register'),
        url(r'^login/$',views.user_login,name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^perfil/$',views.user_profile,name='perfil'),
        url(r'^perfil/edit$',views.user_editData,name='edit'),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': settings.DEBUG}),
    )

urlpatterns += staticfiles_urlpatterns()
