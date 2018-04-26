from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View

from .models import File, User
from .forms import FileForm
from os.path import join, dirname, abspath
import json, xlrd, os

############ Home Page ##################
def index(request):
    # print('helo inddexss')
    return render(request, 'excelFileApp/home.html', {})


############ For Uploading single/multiple file in DB ##################
class FileUploadView(View):
    def get(self, request):
        file_list = File.objects.all()
        return render(self.request, 'excelFileApp/file_upload.html', {'files': file_list})

    def post(self, request):
        form = FileForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        jsonData = json.dumps(data)
        # jsd = json.loads(jsonData)
        self.importData(jsonData)
        return JsonResponse(data)
    
    def importData(self, data):
        data = json.loads(data)
        print('import data')
        print(data['name'])
        cwd = os.getcwd()
        # print(cwd)    # Current Workign Directory
        # filename = join(dirname(dirname(abspath(__file__))), '/media/files/'+data['name'])
        filename = (cwd+'\media\\'+data['name'])
        # print(filename)   # File name
        xl_file = xlrd.open_workbook(filename)
        sheet_names = xl_file.sheet_names()
        xl_sheet = xl_file.sheet_by_name(sheet_names[0])
        # Or grab the first sheet by index 
        #  (sheets are zero-indexed)
        # xl_sheet = xl_file.sheet_by_index(0)
        # print ('Sheet name: %s' % xl_sheet.name)

        row = xl_sheet.row(0)  # 1st row
        # Print 1st row values and types
        print(row)
        # from xlrd.sheet import ctype_text   

        # print('(Column #) type:value')
        # for idx, cell_obj in enumerate(row):
        #     cell_type_str = ctype_text.get(cell_obj.ctype, 'unknown type')
        #     print('(%s) %s %s' % (idx, cell_type_str, cell_obj.value))

        # Print all values, iterating through rows and columns
        num_cols = xl_sheet.ncols   # Number of columns
        num_rows = xl_sheet.nrows   # Number of rows
        values = {}
        # print(num_rows, num_cols) 
        for row_idx in range(1, num_rows):    # Iterate through rows
            print ('-'*40)
            print ('Row: %s' % row_idx)   # Print row number
            for col_idx in range(0, num_cols):  # Iterate through columns
                cell_obj = xl_sheet.cell(row_idx, col_idx)  # Get cell object by row, col
                print ('Column: [%s] cell_obj: [%s]' % (col_idx, cell_obj))
                values[col_idx] = cell_obj.value
                # user = User.objects.create(name=cell_obj)
            # print(values)
            User.objects.create(name = values[0], mobile=values[1], email=values[2])
            # values.save()



############ For deleting all file from DB ##################
def clear_database(request):
    for fs in File.objects.all():
        fs.file.delete()
        fs.delete()
    return redirect(request.POST.get('next'))
    