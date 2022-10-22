from django.db import models
from supers_types.models import Superstypes
# Create your models here.

class Super(models.Model):
    name = models.CharField(max_length=255)
    alter_ego = models.CharField(max_length=255)
    primary_ability = models.CharField(max_length=255)
    secondary_ability = models.CharField(max_length=255)
    supers_types = models.ForeignKey(Superstypes, on_delete=models.CASCADE)
