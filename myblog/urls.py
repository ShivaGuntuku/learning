from django.conf.urls import url
from django.contrib import admin
from myblog.views import post_create,post_detail,post_list,post_update,post_delete


urlpatterns = [
	url(r'^$',post_list, name='list'),
	url(r'^create/$',post_create),
	url(r'^(?P<id>\d+)/$',post_detail, name = 'detail'),
	url(r'^(?P<id>\d+)/edit/$',post_update, name = 'Update'),
	url(r'^(?P<id>\d+)/delete/$',post_delete),
]