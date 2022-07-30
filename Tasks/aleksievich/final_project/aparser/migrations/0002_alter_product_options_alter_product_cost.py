# Generated by Django 4.0.6 on 2022-07-25 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparser', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Цена'),
        ),
    ]