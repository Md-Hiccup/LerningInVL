from django.db import models

# Create your models here.
class Files(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)