from django.db import models
from django.db.models.fields import CharField, EmailField, TextField


class Contact(models.Model):
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=200)
    message=models.TextField()
