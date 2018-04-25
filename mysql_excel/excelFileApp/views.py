from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

from .models import Files
from .forms import FileForm

# Create your views here
def index(request):
    return render(request, 'excelFileApp/base.html', {})


class FileUploadView(View):
    def get(self, request):
        file_list = Files.objects.all()
        return render(self.request, 'excelFileApp/file_upload.html', {'files': file_list})

    def post(self, request):
        form = FileForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)