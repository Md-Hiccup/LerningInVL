from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'files_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('files/file-upload/', views.FileUploadView.as_view(), name='file_upload'),
    path('clear/', views.clear_database, name='clear_database'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
