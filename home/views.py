from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet



# Create your views here.
def home(request):
    current_datetime = datetime.now()
    return render(request, 'home_page.html', {"value": current_datetime})


def landing_page(request):
    return render(request, 'landing_page.html')


def practice_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        staff_id = request.POST.get('staff_id')
        report_details = request.POST.get('details')

    if username and staff_id and report_details:
            report = practice_page(username=username, staff_id=staff_id, details=report_details)
            report.save()
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