from django.contrib import admin
from django.urls import path, include

from . import views as mainviews

urlpatterns = [
    path('home/', mainviews.home),
    path('search/', mainviews.search)
]