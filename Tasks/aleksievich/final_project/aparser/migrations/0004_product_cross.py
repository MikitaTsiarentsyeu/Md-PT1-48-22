# Generated by Django 4.0.6 on 2022-07-26 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparser', '0003_alter_product_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cross',
            field=models.TextField(verbose_name='Кросс'),
            preserve_default=False,
        ),
    ]