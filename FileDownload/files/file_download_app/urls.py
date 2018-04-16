from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('download/excel/', views.download_in_excel, name='download_in_excel'),
    path('download/pdf/', views.download_in_pdf, name='download_in_pdf'),
]