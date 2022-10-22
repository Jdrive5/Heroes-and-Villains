from django.db import models

# Create your models here.

class Superstypes(models.Model):
    type = models.CharField(max_length=255)