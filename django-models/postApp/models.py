from django.db import models


# Create your models here.
class Post(models.Model):
    header = models.CharField(max_length=255)
    content = models.TextField()
    is_publish = models.BooleanField()
    date = models.DateField()
