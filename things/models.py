from django.db import models    
from  django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.TextField(blank=True, max_length=120, unique=False)
    quantity = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(0), MinValueValidator(100)])
