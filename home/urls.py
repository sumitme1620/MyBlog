from django.contrib import admin
from django.urls import path
from .views import home, about, contact, post, category


urlpatterns = [
    path("", home),
    path("home/", home),
    path("about/", about),
    path("contact/", contact),
    path("blog/<slug:url>", post),
    path("category/<slug:url>", category),
]
