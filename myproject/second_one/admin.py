from .models import Products
from django.contrib import admin

# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id','title','price','color','image')

admin.site.register(Products,ProductsAdmin)

