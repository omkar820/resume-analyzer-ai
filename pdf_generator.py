from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf_report(text, filename="Resume_Feedback.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    textobject = c.beginText(50, height - 50)
    textobject.setFont("Helvetica", 10)

    for line in text.split('\n'):
        textobject.textLine(line)

    c.drawText(textobject)
    c.save()
    return filename
