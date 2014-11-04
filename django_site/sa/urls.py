from django.conf.urls import patterns, url
from django.conf import settings

from sa import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    #url(r'^$', views.index),
)
