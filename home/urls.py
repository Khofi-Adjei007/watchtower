from . import views
from django.http import HttpResponse
from django.urls import path


urlpatterns = [
    path('home_page/', views.home),
    path('landing_page/', views.landing_page),
    path('practice_page/', views.practice_page),
    path('submissionpdf/', views.submissionpdf, name='submissionpdf'),
]