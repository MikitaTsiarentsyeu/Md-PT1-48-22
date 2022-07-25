from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.CharField(max_length=200, blank=False)
    image = models.ImageField(upload_to='img')

    def __str__(self):
        return self.name

class Lection(models.Model):
    title = models.CharField(max_length=80, blank=False)
    text = models.TextField(blank=True)
    video = models.FileField(upload_to='videos', validators=[FileExtensionValidator(allowed_extensions=['mp4','webm'])])

    course = models.ForeignKey(Course, on_delete = models.CASCADE)

    def __str__(self):
        return self.title