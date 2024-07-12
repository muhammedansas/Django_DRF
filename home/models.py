from django.db import models

# Create your models here.

class Persons(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    place = models.CharField(max_length=100)

class Workers(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    place = models.CharField(max_length=100) 
       