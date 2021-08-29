from django.db import models

# Create your models here.

class Contacts(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField()
    message=models.TextField()