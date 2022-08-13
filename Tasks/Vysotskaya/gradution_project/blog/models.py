from distutils.command.upload import upload
import email
from email.mime import image
from email.policy import default
from turtle import title
from django.db import models
from django.db import models
from datetime import datetime
from calendar import Calendar
from calendar import calendar

class Author(models.Model): 
    name = models.CharField(blank=False, max_length=100)
    email = models.EmailField(blank=False, primary_key=True)

    def __str__(self) :
        return self.email

class Post(models.Model): 

    POST_TYPES = [('c', 'copyright'), ('a', 'author')]

    title = models.CharField(blank=False, max_length=100)
    content = models.TextField(blank=False)
    issued = models.DateTimeField()
    image = models.ImageField(upload_to= 'uploads')

    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    
    def __str__(self) :
        return self.title 


class History(models.Model): 

    title = models.CharField(blank=False, max_length=100)
    history = models.TextField(blank=False)
    date = models.DateTimeField()
    image_history = models.ImageField(upload_to= 'hitory/image', default="", blank=True)
 
    def __str__(self) :
        return self.title 


class Services(models.Model): 

    title = models.CharField(blank=False, max_length=100)
    services = models.TextField(blank=False)
    image_services = models.ImageField(upload_to= 'services/image', default="", blank=True)
 
    def __str__(self):
        return self.title 
    


   