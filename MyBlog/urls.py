"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#coding=utf-8
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve

from blog.views import *
from MyBlog.settings import MEDIA_ROOT
from MyBlog.feeds import LatestEntriesFeed


urlpatterns = [
    url(r'^$', bloglist, name=''),
    url(r'^blog/(?P<id>\w+)$', blog, name='blog'),
    url(r'^blog/(?P<s>\w+)$', blog, name='s'),
    url(r'^admin/', admin.site.urls),

    url(r'^media/(?P<path>.*)$',  serve, {"document_root":MEDIA_ROOT}, name='media'),
    url(r'^rss$', LatestEntriesFeed(), name='rss'),#rss
    

    url(r'^robots\.txt$', robots), #robots

    url(r'^test', test, name='test'),

    url(r'^sitemap\.xml$', sitemap),


]

handler403 = permission_denied
handler404 = page_not_found
handler500 = page_error
