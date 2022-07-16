import email
from pyexpat import model
from django.db import models

class Author(models.Model):

    name = models.CharField(blank=False, max_length=100)
    email = models.EmailField(blank=False, primary_key=True)

    def __str__(self):
        return self.email

class Post(models.Model):

    POST_TYPES = [('c', 'copyright'), ('a', 'author')]

    title = models.CharField(blank=False, max_length=200)
    subtitle = models.CharField(max_length=500)
    content = models.TextField(blank=False)
    issued = models.DateTimeField()
    post_type = models.CharField(max_length=1, blank=False, choices=POST_TYPES)
    image = models.ImageField(upload_to='uploads')

    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

