from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render
from xhtml2pdf import pisa
# Create your views here.

def generate_pdf(html):
    # Create the HttpResponse object with PDF headers.
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="Probne.pdf"'

    # Create the PDF object, using the StringIO object as its "file."
    pdf = pisa.CreatePDF(html, dest=response)

    if not pdf.err:
        return response

    return HttpResponse('Error generating PDF file.')

def say_hello(request):
    template = get_template('hello.html')
    context = {'name': ''}
    html = template.render(context)
    #return render(request, 'hello.html', {'name': 'Kornel'})
    return generate_pdf(html)



