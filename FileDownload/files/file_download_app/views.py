from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
# from django.utils import timezone

#   For Downloading File in Excel and Pdf
import xlwt 
from io import BytesIO 
from reportlab.pdfgen import canvas 

#   For Searching File
# import json
from django.core.serializers import serialize

from .models import Book, Document
from .forms import BookForm, DocumentForm


###############   Home Page   #######################

def index(request):
    # For displaying data on Home page
    context = (Book.objects.values())

    # For autocomplete search box
    data = serialize('json', Book.objects.all())

    return render(request, 'file/home.html', { 'data': data, 'context': context})
    # return HttpResponse("Welcome to home")


###############   For Adding a new Book   #######################

def new_book(request):     
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            # book.author = request.user
            book.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'file/create.html', {'form': form})

###############   Getting Detail of particular Book #######################

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'file/detail.html', {'book': book})

###############   For Editing a Particular Book   #######################

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'file/create.html', { 'form': form })

###############   For Deleting a Particular Book   #######################

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('crud_task')


############## Download File in Excel ##########################

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


############## Download File in Pdf ##########################

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

############## Download File in Simple Format ##########################

def download_in_file(request):
    return HttpResponse("Download File in simple format")

############## Download File in CSV forat ##########################

def download_in_csv(request):
    return HttpResponse("Download File in csv format")

############## Download File in JSON format ##########################

def download_in_json(request):
    return HttpResponse("Download File in json format")




############# Upload File ##########################################

def uploadfile(request):
    documents = Document.objects.all()
    return render(request, 'file/files.html', { 'documents' :  documents }) 

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('uploadfile')
    else:
        form = DocumentForm()
    return render(request, 'file/upload.html', {
        'form': form
    })

