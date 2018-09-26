from django.conf.urls import url
from django.contrib import admin, messages
from django.http import HttpResponse
from django.shortcuts import render


def produce_message(request):
    messages.info(request, "Default messages framework")
    return HttpResponse("OK")


urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^$", lambda request: render(request, "base.html")),
    url(r"^produce_message/$", produce_message),
    url(r"^404/$", lambda request: render(request, "404.html")),
]
