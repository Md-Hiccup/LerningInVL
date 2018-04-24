from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'photos'

urlpatterns = [
    path('clear/', views.clear_database, name='clear_database'),
    path('basic-upload/', views.BasicUploadView.as_view(), name='basic_upload'),
    path('progress-bar-upload/', views.ProgressBarUploadView.as_view(), name='progress_bar_upload'),
    path('drag-and-drop-upload/', views.DragAndDropUploadView.as_view(), name='drag_and_drop_upload'),
    
    # url(r'^clear/$', views.clear_database, name='clear_database'),
    # url(r'^basic-upload/$', views.BasicUploadView.as_view(), name='basic_upload'),
    # url(r'^progress-bar-upload/$', views.ProgressBarUploadView.as_view(), name='progress_bar_upload'),
    # url(r'^drag-and-drop-upload/$', views.DragAndDropUploadView.as_view(), name='drag_and_drop_upload'),

]
