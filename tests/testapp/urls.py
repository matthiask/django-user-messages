from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import render


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', lambda request: render(request, 'base.html')),
    url(r'^404/$', lambda request: render(request, '404.html')),
]
