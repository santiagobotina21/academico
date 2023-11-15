from django.db import models
from django.utils import timezone
import datetime 

class User(models.Model):
    email=models.CharField(max_length=100,null=False)
    password=models.CharField(max_length=500, null=False)
    status=models.BooleanField(default=True, null=True)
    created_at=models.DateTimeField(default=datetime.datetime.now, null=False)
    update_at=models.DateTimeField(default=datetime.datetime.now, null=False)
    deleted_at=models.DateTimeField(null=True)

class identification_types(models.Model):
    name=models.CharField(max_length=50,null=False)
    abrev=models.CharField(max_length=10, null=False)
    descrip=models.CharField(max_length=100, null=False)
    created_at=models.DateTimeField(default=datetime.datetime.now, null=False)
    update_at=models.DateTimeField(default=datetime.datetime.now, null=False)
    deleted_at=models.DateTimeField(null=True)
    
# Create your models here.
