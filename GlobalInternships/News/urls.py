from django.conf.urls import patterns, url

from News import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<news_id>\d+)/$', views.detail, name='detail'),
)
