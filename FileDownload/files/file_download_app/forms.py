from django import forms
from django.forms import TextInput

from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'author', 'price')
        