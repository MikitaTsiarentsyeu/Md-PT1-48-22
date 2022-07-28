from django.db import models

class Books(models.Model):
    series = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    image = models.ImageField(blank=True,upload_to='uploads/books')
    url_book = models.URLField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name



class Theme(models.Model):
    title = models.CharField(blank=False,max_length=200)
    create = models.DateTimeField(auto_now_add=True)
    change = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class Information(models.Model):
    content = models.TextField(blank=True)
    images = models.ImageField(blank=True, upload_to='uploads/images/%y/%m/')
    #files = models.FileField(upload_to='uploads/files/%y/%m/')
    create = models.DateTimeField(auto_now_add=True)
    theme = models.ForeignKey('Theme', on_delete=models.CASCADE)
    author = models.CharField(max_length=50, default='author')