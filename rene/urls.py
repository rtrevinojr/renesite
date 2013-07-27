
from django.conf.urls import patterns, include, url
from rene import views
from views import *

urlpatterns = patterns('',
		
	url(r'^$', views.index, name='index'),
	#url(r'^/rene/bio/$', views.bio, name='bio'),		

)
