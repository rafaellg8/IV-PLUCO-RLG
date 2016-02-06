"""pluco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from foros import views
from registration.backends.simple.views import RegistrationView
from plucoApp.forms import userForms
from django.conf import settings
# Clase que redirige a la pagina principal a un usuario que se ha registrado
class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/'


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project_17.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^plucoApp/', include('plucoApp.urls')),
    url(r'^', include('plucoApp.urls')),
    url(r'^foros/',include('foros.urls')),
    url(r'^comentario/',include('foros.urls')),
    url(r'^foros/theme/(?P<theme>[\w\-]+)/nuevoComentario', views.comment, name='theme'),
    url(r'^accounts/register/$', MyRegistrationView.as_view(form_class=userForms), name='registration_register'),
    (r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': settings.DEBUG}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),
)
urlpatterns += staticfiles_urlpatterns()

     # ADD THIS NEW TUPLE!
