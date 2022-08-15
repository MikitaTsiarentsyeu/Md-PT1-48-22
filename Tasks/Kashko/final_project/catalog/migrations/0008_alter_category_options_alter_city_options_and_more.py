# Generated by Django 4.0.6 on 2022-08-08 19:08

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_contact_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['name'], 'verbose_name_plural': 'cities'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['last_name']},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['create_date']},
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Phone number', max_length=128, region='BY'),
        ),
    ]
