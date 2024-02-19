from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('firstpage/',views.firstpage,name='firstpage')
]   