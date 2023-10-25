from django.db import models

class User(models.Model):
    emai=models.CharField(max_length=100)
    password=models.CharField(max_length=500)
# Create your models here.
