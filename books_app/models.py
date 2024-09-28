from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    publication_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title