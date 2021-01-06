from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    category = models.CharField(max_length=64, default='None')
    book_cover = models.TextField(default='no-image-available.png')
    price = models.IntegerField()
    description = models.TextField()
    DEFAULT_ID = 1
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
