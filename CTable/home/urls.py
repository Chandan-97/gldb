from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('campaign/', views.campaign),
    path('criteria/', views.criteria),
    path('logout', views.Logout),
    path('selection/', views.selection),
    path('confirm/', views.confirm),
    path('test/', views.test),
]