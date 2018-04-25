from django.contrib import admin

from .models import Book, Document, Photo

# Register your models here.
admin.site.register(Book)
admin.site.register(Document)
admin.site.register(Photo)