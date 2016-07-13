from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^info/(?P<link_id>[0-9]+)/$', views.info, name='info'),
    url(r'^$', views.index, name='index')
]