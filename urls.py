from django.conf.urls.defaults import patterns, include, url
from rene import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'rene.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^rene/$', include('rene.urls') ),
    #url(r'^(rene)?/?$', 'views.index', name='index'),
    #url(r'^(rene)?/bio/$', 'rene.views.bio', name='bio' ),
)
