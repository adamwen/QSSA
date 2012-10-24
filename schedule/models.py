from django.db import models

# Create your models here.

class Info(models.Model):
    schoolId = models.CharField(max_length=200)
    pw = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
