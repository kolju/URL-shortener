from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^delete/(?P<link_id>[0-9]+)/$', views.delete_obj, name='delete_obj'),
    url(r'^overall/$', views.overall, name='overall'),
    url(r'^info/(?P<link_id>[0-9]+)/$', views.info, name='info'),
    url(r'^$', views.index, name='index'),
    url(r'(?P<short_url>[0-9A-Za-z]+)/$', views.url_redirect, name='url_redirect')
]