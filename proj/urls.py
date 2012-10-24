from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^submit$','schedule.views.submit'),
    url(r'^$','schedule.views.index'),
    url(r'assets/(?P<path>.*)$','django.views.static.serve',{'document_root': './templates/assets/'}),
    url(r'static/(?P<path>.*)$','django.views.static.serve',{'document_root': './templates/static/'}),
    url(r'^gloginwrong/$','schedule.views.gloginwrong'),
    url(r'^sloginwrong/$','schedule.views.sloginwrong'),
    url(r'^about/$','schedule.views.about'),
    url(r'^index/$','schedule.views.index'),
    #url(r'^index/assets/js/(?P<path>.*)$','django.views.static.serve',{'document_root': '/home/adam/Dropbox/code/django/proj/templates/assets/js/'}),
    #url(r'^index/assets/js/(?P<path>.*)$','django.views.static.serve',{'document_root': '/home/adam/Dropbox/code/django/proj/templates/assets/js/'}),

    # Examples:
    # url(r'^$', 'proj.views.home', name='home'),
    # url(r'^proj/', include('proj.foo.urls')),
      
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
