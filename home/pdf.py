from reportlab.pdfgen import canvas

def hello(c):
    content = ["Feature One", "Feature Two", "Feature Three"]
    c.drawString(200,200, f"{content}")

c = canvas.Canvas("Kings.pdf")
hello(c)
c.showPage()
c.save()