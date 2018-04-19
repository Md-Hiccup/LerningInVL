from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    #   Add, Detial, Edit and Delete a book
    path('book/new/', views.new_book, name='new_book'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('book/delete/<int:pk>/', views.delete_book, name='delete_book'),

    #   Download File in Excel and Pdf
    path('download/excel/', views.download_in_excel, name='download_in_excel'),
    path('download/pdf/', views.download_in_pdf, name='download_in_pdf'),

    #   Search Book from DB
    path('api/get_book_names/', views.get_book_names, name='get_book_names'),
]