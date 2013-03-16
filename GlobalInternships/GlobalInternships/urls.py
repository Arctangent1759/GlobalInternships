from django.conf.urls import patterns, include, url
from django.shortcuts import render

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GlobalInternships.views.home', name='home'),
    # url(r'^GlobalInternships/', include('GlobalInternships.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^news/',include('News.urls', namespace='News')),
	url(r'^event/',include('Event.urls', namespace='Event')),
	url(r'^board/$', lambda request:render(request,'Static/board.html')),
	url(r'^about/$', lambda request:render(request,'Static/about.html')),
	url(r'^$',include('News.urls', namespace='News')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
