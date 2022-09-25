from django.contrib import admin, messages
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path


def produce_message(request):
    messages.info(request, "Default messages framework")
    return HttpResponse("OK")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", lambda request: render(request, "base.html")),
    path("produce_message/", produce_message),
    path("404/", lambda request: render(request, "404.html")),
]
