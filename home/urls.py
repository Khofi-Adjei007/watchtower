from . import views
from django.http import HttpResponse
from django.urls import path

urlpatterns = [
    path('home_page/', views.home)
]