from django.conf.urls import patterns
from django.conf.urls import url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from foros import views

urlpatterns = patterns('',
    url(r'(?P<theme>[\w\-]+)/nuevoComentario', views.comment, name='comment'),
    url(r'(?P<slug>[\w\-]+)/$', views.numberVisits, name='slug'),
    url(r'reclama_datos',views.getVisits,name='graphic'),
    url(r'like',views.like_comment,name='like'),
    url(r'^$', views.showForums, name='forums'),
    url(r'^foros', views.showForums, name='comment'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': settings.DEBUG}),
)

urlpatterns += staticfiles_urlpatterns()
