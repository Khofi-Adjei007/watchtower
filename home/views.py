from django.shortcuts import render
from datetime import datetime


# Create your views here.
def home(request):
    current_datetime = datetime.now()
    return render(request, 'home_page.html', {"value": current_datetime})


def landing_page(request):
    return render(request, 'landing_page.html')

def counter(request):
    pass


def submissionpdf(request):
   text = request.POST['docket_forms']
   amount_of_words = len(text.split())
   return render(request, 'submissionpdf.html', {"amount": amount_of_words})