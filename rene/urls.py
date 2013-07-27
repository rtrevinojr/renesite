
from django.conf.urls.defaults import patterns, include, url

from rene import views

urlpatterns = patterns('',
		
	url(r'^$', views.index, name='index'),
	#url(r'^/rene/bio/$', views.bio, name='bio'),		

)
