from django.urls import path

from . import views

urlpatterns = [
    path('', views.crud_task, name='crud_task'),
    path('book/new/', views.create_book, name='create_book'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('book/delete/<int:pk>/', views.delete_book, name='delete_book'),
	path('download/excel/', views.download_in_excel, name='download_in_excel'),
	path('download/pdf/', views.download_in_pdf, name='download_in_pdf'),
]