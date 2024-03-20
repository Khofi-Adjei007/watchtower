from reportlab.pdfgen import canvas


fileName = "firstpdf.pdf"
documentTitle = "Sgn/Adjeteh/02/03/2024"

pdf = canvas.Canvas(fileName)
pdf.setTitle(documentTitle)
pdf.save()