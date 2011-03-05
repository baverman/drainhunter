from django.conf.urls.defaults import *
from drainhunter.django import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='drainhunter-index'),
    url(r'^snapshot/$', views.take_snapshot, name='drainhunter-snapshot'),
    url(r'^list/(.+)\.(svg|png|dot)$', views.object_list, name='drainhunter-list'),
)