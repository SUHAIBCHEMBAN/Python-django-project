# Generated by Django 5.0.2 on 2024-02-15 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('second_one', '0003_products_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='image',
        ),
    ]
