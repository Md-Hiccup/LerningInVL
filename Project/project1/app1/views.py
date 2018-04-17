from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Book
from .forms import BookForm

import xlwt

############ CRUD TASK #################################
# Create your views here.
def crud_task(request):
    cruds = Book.objects.all()
    return render(request, 'app1/read.html', { 'cruds': cruds })

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'app1/detail.html', {'book': book})

def create_book(request):
    # return render(request, 'crudapp/create.html', { })
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            # book.author = request.user
            book.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'app1/create.html', {'form': form})

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
    return render(request, 'app1/create.html', { 'form': form })

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('crud_task')

############################################################

################# DOWNLOAD TASK ############################

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
    return HttpResponse("Download file in pdf")

############################################################
