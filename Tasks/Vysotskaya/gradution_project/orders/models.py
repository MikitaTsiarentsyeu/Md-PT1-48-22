from django.db import models
from blog.models import Services


class Order(models.Model):
    service = models.ForeignKey(Services, verbose_name='Services', on_delete=models.CASCADE)
    name = models.CharField("name", max_length=50)
    phone = models.CharField("phone", max_length=50)
    data = models.DateField('data', auto_now_add=True)
