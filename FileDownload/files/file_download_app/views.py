from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.utils import timezone

import xlwt # for excel 
from io import BytesIO
from reportlab.pdfgen import canvas # for pdf 

# from reportlab.lib import colors
# from reportlab.lib.pagesizes import letter, inch
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

from .models import Book

# Create your views here.
def index(request):
    content = Book.objects.all()
    return render(request, 'file/home.html', { 'content': content })
    # return HttpResponse("Welcome to home")


def download_in_excel(request):
    # content-type of response
    response = HttpResponse(content_type='application/ms-excel')
 
    #decide file name
    response['Content-Disposition'] = 'attachment; filename="ThePythonDjango.xls"'
 
    #creating workbook
    wb = xlwt.Workbook(encoding='utf-8')
 
    #adding sheet
    ws = wb.add_sheet("sheet1")
 
    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    # headers are bold
    font_style.font.bold = True
 
    #column header names, you can use your own headers here
    columns = ['Name', 'Author', 'Price', ]
 
    #write column headers in sheet
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
 
    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
 
    #get your data, from database or from a text file...
    data = Book.objects.all() #dummy method to fetch data.
    for my_row in data:
        row_num = row_num + 1
        ws.write(row_num, 0, my_row.name, font_style)
        ws.write(row_num, 1, my_row.author, font_style)
        ws.write(row_num, 2, my_row.price, font_style)
        # ws.write(row_num, 3, my_row.notes, font_style)
 
    wb.save(response)
    return response



def download_in_pdf(request):
   # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    buffer = BytesIO()
    # Create the PDF object, using the BytesIO object as its "file."
    p = canvas.Canvas(buffer)
    
    # data = Book.objects.all()    
    # p = canvas.Canvas(data, pagesize=letter)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100 , 100 , "Hello World")

    # Close the PDF object cleanly.
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response


# def download_in_pdf(request):
#     # response = HttpResponse(content_type='application/pdf')
#     # response['Content-Disposition'] = 'attachment'
#     doc = SimpleDocTemplate("file_name.pdf", pagesize=letter)

#     elements = []
#     data= [['00', '01', '02', '03', '04'],
#        ['10', '11', '12', '13', '14'],
#        ['20', '21', '22', '23', '24'],
#        ['30', '31', '32', '33', '34']]
#     t=Table(data,5*[0.4*inch], 4*[0.4*inch])
#     t.setStyle(TableStyle([
#         ('ALIGN',(1,1),(-2,-2),'RIGHT'),
#         ('TEXTCOLOR',(1,1),(-2,-2),colors.red),
#         ('VALIGN',(0,0),(0,-1),'TOP'),
#         ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
#         ('ALIGN',(0,-1),(-1,-1),'CENTER'),
#         ('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
#         ('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
#         ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
#         ('BOX', (0,0), (-1,-1), 0.25, colors.black),
#         ]))
 
#     elements.append(t)
#     # write the document to disk
#     doc.build(elements)