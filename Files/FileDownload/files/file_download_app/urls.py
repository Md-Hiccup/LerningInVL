from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'photos'

urlpatterns = [
    path('', views.index, name='index'),
    
    #   Add, Detial, Edit and Delete a book
    path('book/new/', views.new_book, name='new_book'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('book/delete/<int:pk>/', views.delete_book, name='delete_book'),

    #   Download File in Simple Flat file, CSV, Json, Excel, and Pdf format

    # path('download/file/', views.download_in_file, name='download_in_file'),
    # path('download/csv/', views.download_in_csv, name='download_in_csv'),
    # path('download/json/', views.download_in_json, name='download_in_json'),
    path('download/excel/', views.download_in_excel, name='download_in_excel'),
    path('download/pdf/', views.download_in_pdf, name='download_in_pdf'),

    path('upload/', views.uploadfile, name='uploadfile'),
    # path('upload/demofile', views.upload_file, name='upload_file'),
    path('upload/fileupload/', views.model_form_upload, name='model_form_upload'),
    path('multipleupload/', views.multiple_upload, name='multiple_upload'), 

    path('photos/clear/', views.clear_database, name='clear_database'),
    path('photos/basic-upload/', views.BasicUploadView.as_view(), name='basic_upload'),
    path('photos/progress-bar-upload/', views.ProgressBarUploadView.as_view(), name='progress_bar_upload'),
    path('photos/drag-and-drop-upload/', views.DragAndDropUploadView.as_view(), name='drag_and_drop_upload'),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

