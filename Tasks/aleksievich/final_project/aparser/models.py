from tabnanny import verbose
from turtle import title
from django.db import models

class Product (models.Model):
    article = models.TextField(
    verbose_name='Артикул',
    )
    brend = models.TextField(
        verbose_name='Бренд',
    )
    cross = models.TextField(
        verbose_name='Кросс',
        unique=True,
    )
    quantity = models.TextField(
        verbose_name='Количество',
    )
    cost = models.DecimalField(
        verbose_name='Цена', max_digits=5, decimal_places=2,
    )
    parsing_date = models.DateTimeField(
        verbose_name='Дата парсинга'
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
