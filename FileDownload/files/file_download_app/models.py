from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Document(models.Model):
    # title = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    # document = models.FileField(upload_to='documents/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

