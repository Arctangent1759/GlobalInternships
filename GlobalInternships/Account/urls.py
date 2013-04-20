from django.conf.urls import patterns, url

from Account import views

urlpatterns = patterns('',
	url(r'^activate/(?P<user_id>\d+)/$', views.activate, name='user'),
	url(r'^create/$', views.create, name='event'),
)
