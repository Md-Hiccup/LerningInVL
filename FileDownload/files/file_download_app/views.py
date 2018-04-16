from django.shortcuts import render
from django.http import HttpResponse

import xlwt # for excel 

from reportlab.pdfgen import canvas # for pdf 

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
    # font_style = xlwt.XFStyle()
 
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
    return HttpResponse("Download file in pdf")

