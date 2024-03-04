from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home_page.html')


def landing_page(request):
    return render(request, 'landing_page.html')
