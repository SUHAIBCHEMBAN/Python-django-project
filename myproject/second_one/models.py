from django.db import models

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length = 35)
    price = models.IntegerField()
    color = models.CharField(max_length=50)
    image = models.ImageField(upload_to='django img')