import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


def employees_pdf(request):

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter, bottomup=0)

    textobject = p.beginText()
    textobject.setTextOrigin(inch, inch)
    textobject.setFont("Helvetica", 13)

    employee_list = [
        {"name": "John", "age": 23},
        {"name": "Robert", "age": 25},
        {"name": "Jim", "age": 37},
        {"name": "Ron", "age": 37},
        {"name": "Rafael", "age": 37},
        {"name": "Jamal", "age": 37},
    ]

    for line in employee_list:
        l = 'name={0} - age={1}'.format(line["name"], line["age"])
        textobject.textLine(l)

    p.drawText(textobject)
    p.showPage()
    p.save()
    buffer.seek(0)

    return FileResponse(buffer, as_attachment=True, filename='employees_pdf.pdf')
