from django.conf.urls import patterns, url

from Event import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<event_id>\d+)/$', views.event, name='event'),
)
