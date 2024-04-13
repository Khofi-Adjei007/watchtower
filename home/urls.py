from . import views
from django.http import HttpResponse
from django.urls import path


urlpatterns = [
    path('home_page/', views.home, name='home_page'),
    path('login_screen/', views.login_screen),
    path('registrations/', views.registrations),
    path('submissionpdf/', views.submissionpdf, name='submissionpdf'),
]