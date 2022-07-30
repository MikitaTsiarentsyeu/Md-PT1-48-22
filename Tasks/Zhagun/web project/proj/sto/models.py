
from django.db import models

class registration(models.Model):
    name = models.CharField(blank=False,max_length=100, verbose_name='Имя')
    phone = models.CharField(blank=False,max_length = 13, verbose_name='Телефон')
    auto = models.CharField(blank=False,max_length=200, verbose_name='Марка и модель авто')
    year = models.CharField(blank=False,max_length=4, verbose_name='Год авто')
    service = models.CharField(blank=False,max_length=200, verbose_name='Услуги')
    comment = models.TextField(blank=False, verbose_name='Комментарий')

    def __str__(self):
        return self.name



    

