from django.contrib import admin, messages
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import re_path


def produce_message(request):
    messages.info(request, "Default messages framework")
    return HttpResponse("OK")


urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    re_path(r"^$", lambda request: render(request, "base.html")),
    re_path(r"^produce_message/$", produce_message),
    re_path(r"^404/$", lambda request: render(request, "404.html")),
]
