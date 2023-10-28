from django.db import models

class User(models.Model):
    emai=models.CharField(max_length=100)
    password=models.CharField(max_length=500)
    dni=models.CharField(max_length=10,default='')
# Create your models here.
