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



# Create your views here.
def home(request):
    current_datetime = datetime.now()
    return render(request, 'home_page.html', {"value": current_datetime})


def landing_page(request):
    return render(request, 'landing_page.html')




def practice_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_two = request.POST.get('password_two')

        # Check if any of the fields are empty
        if not (password and username and email and password_two):
            empty_field_error = 'All fields must be filled.'
            return render(request, 'practice_page.html', {'empty_field_error': empty_field_error})

        # Check if passwords match
        if password != password_two:
            password_mismatch_error = 'Passwords do not match.'
            return render(request, 'practice_page.html', {'password_mismatch_error': password_mismatch_error})

        # Check password complexity requirements
        special_chars = set(string.punctuation)
        num_chars = set(string.digits)
        uppercase_chars = set(string.ascii_uppercase)
        password_set = set(password)
        if not (special_chars & password_set and num_chars & password_set and uppercase_chars & password_set):
            password_complexity_error = 'Password must contain at least one special character, one digit, and one uppercase letter.'
            return render(request, 'practice_page.html', {'password_complexity_error': password_complexity_error})

        # Check if email or username already exists
        if User.objects.filter(email=email).exists():
            email_exists_error = 'This email has already been used.'
            return render(request, 'practice_page.html', {'email_exists_error': email_exists_error})
        elif User.objects.filter(username=username).exists():
            username_exists_error = 'Username already exists.'
            return render(request, 'practice_page.html', {'username_exists_error': username_exists_error})

        # Create user if all checks pass
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        messages.success(request, 'Account created successfully!')
        return redirect('success_page')  # Redirect to a success page

    # If GET request or form submission failed, render the form page
    return render(request, 'practice_page.html')






def submissionpdf(request):
    if request.method == 'POST':
        text = request.POST.get('docket_forms', '')

        # Generate PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="submission_{datetime.now().strftime("%Y-%m-%d")}.pdf"'

        doc = SimpleDocTemplate(response, pagesize=letter)
        styles = getSampleStyleSheet()
        style_normal = styles['Normal']

        content = []
        content.append(Paragraph("Form Content:", style_normal))
        content.append(Spacer(1, 12))
        content.append(Paragraph(text, style_normal))

        doc.build(content)
        
        return response

    else:
        return HttpResponse("This view only accepts POST requests.")