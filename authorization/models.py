from django.db import models


# Create your models here.

class Person(models.Model):
    email = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50, unique=False)
