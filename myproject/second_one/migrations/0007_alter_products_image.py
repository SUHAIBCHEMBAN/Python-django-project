# Generated by Django 5.0.2 on 2024-02-15 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_one', '0006_alter_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='django img'),
        ),
    ]