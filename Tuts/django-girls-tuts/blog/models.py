from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):           #   defines our model(it is an object) and models.Model means Post is a Django Model, so Django knows that it should be saved in the database.
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)      # Charecter Field
    text = models.TextField()                       # Text Field
    created_date = models.DateTimeField( default = timezone.now)    # Date time Field
    published_date = models.DateTimeField( blank = True, null = True)   # Date time Field

    def publish(self):              #   Post method
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):              #   for readable in shell
        return self.title