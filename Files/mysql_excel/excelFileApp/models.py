from django.db import models
import uuid
# Create your models here.
class File(models.Model):
    # title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        filename = str(self.file)
        return filename

class User(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4 )
    name = models.CharField(max_length=255)
    mobile = models.DecimalField(max_digits=12, decimal_places=0)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.name