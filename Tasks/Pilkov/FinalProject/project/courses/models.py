from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=200, blank=False)


class Lection(models.Model):
    title = models.CharField(max_length=80, blank=False)
    subtitle = models.CharField(max_length=100, blank=False)
    text = models.TextField(blank=True)
    video = models.FileField(upload_to='uploads', validators=[FileExtensionValidator(allowed_extensions=['mp4','webm'])])

    course = models.ForeignKey(Course, on_delete = models.CASCADE)