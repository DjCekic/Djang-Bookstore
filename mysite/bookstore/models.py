from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    category = models.CharField(max_length=64, default='None')
    book_cover = models.TextField(default='no-image-available.png')
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title

