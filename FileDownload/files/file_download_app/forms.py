from django import forms
from django.forms import TextInput

from .models import Book, Document

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'author', 'price')
        
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ( 'document', )

