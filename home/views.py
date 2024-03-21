from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from django.shortcuts import redirect
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageTemplate
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus.flowables import Flowable



# Create your views here.
def home(request):
    current_datetime = datetime.now()
    return render(request, 'home_page.html', {"value": current_datetime})


def landing_page(request):
    return render(request, 'landing_page.html')

def counter(request):
    pass

class Header(Flowable):
    def __init__(self, width, height, title):
        super().__init__()
        self.width = width
        self.height = height
        self.title = title

    def draw(self):
        self.canv.saveState()
        self.canv.setFillColor(colors.gray)
        self.canv.rect(0, self.height, self.width, self.height, fill=True)
        self.canv.setFont("Helvetica-Bold", 16)
        self.canv.setFillColor(colors.white)
        self.canv.drawString(inch, self.height + 0.4 * inch, self.title)
        self.canv.restoreState()


class Footer(Flowable):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def draw(self):
        self.canv.saveState()
        self.canv.setFillColor(colors.gray)
        self.canv.rect(0, 0, self.width, self.height, fill=True)
        self.canv.restoreState()


def submissionpdf(request):
    if request.method == 'POST':
        text = request.POST.get('docket_forms', '')

        # Generate PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="submission_{datetime.now().strftime("%Y-%m-%d")}.pdf"'

        doc = SimpleDocTemplate(response, pagesize=letter)

        # Header and Footer
        header = Header(doc.width, inch, "Custom Header")
        footer = Footer(doc.width, inch)

        # Create a PageTemplate and add Header/Footer
        template = PageTemplate(id='headerfooter', frames=[header, footer], onPage=headerFooter)
        doc.addPageTemplates(template)

        styles = getSampleStyleSheet()
        style_normal = styles['Normal']

        content = []
        content.append(Paragraph("Form Content:", style_normal))
        content.append(Spacer(1, 12))
        content.append(Paragraph(text, style_normal))

        doc.build(content)

        # Redirect to the same page after processing the form
        return redirect('submissionpdf')

    else:
        return HttpResponse("This view only accepts POST requests.")

def headerFooter(canvas, doc):
    canvas.saveState()

    # Header
    header_text = "This is a header"
    canvas.drawCentredString(doc.pagesize[0] / 2, doc.pagesize[1] - 0.75 * inch, header_text)

    # Footer
    footer_text = "This is a footer"
    canvas.setFont("Helvetica", 9)
    canvas.drawString(inch, 0.75 * inch, footer_text)

    canvas.restoreState()