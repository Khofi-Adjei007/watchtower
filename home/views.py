from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from .models import practice_data
from django.contrib import messages
from django.contrib.auth.models import User, auth
import string
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    current_datetime = datetime.now()
    return render(request, 'home_page.html', {"value": current_datetime})



def practice_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_two = request.POST.get('password_two')

        # Check if any of the fields are empty
        if not all([username, email, password, password_two]):
            empty_field_error = 'All fields must be filled.'
            return render(request, 'practice_page.html', {'empty_field_error': empty_field_error})
        
          # Check if passwords match
        if password != password_two:
            password_mismatch_error = 'Passwords do not match.'
            return render(request, 'practice_page.html', {'password_mismatch_error': password_mismatch_error})

        # Create user if all checks pass
        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Account created successfully!')
        return redirect('home_page')  # Redirect to a success page

    # If GET request or form submission failed, render the form page
    return render(request, 'practice_page.html')



def login_screen(request):
    return render(request, 'login_screen.html')


def submissionpdf(request):
    pass