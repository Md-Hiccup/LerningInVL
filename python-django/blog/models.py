from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):           #   defines our model(it is an object) and models.Model means Post is a Django Model, so Django knows that it should be saved in the database.
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField( default = timezone.now)
    published_date = models.DateTimeField( blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title