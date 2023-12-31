from django.db import models

# Create your models here.

class Word(models.Model):
    text=models.TextField(null=True,blank=True)
