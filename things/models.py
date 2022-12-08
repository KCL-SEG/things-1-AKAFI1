from django.db import models    

# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True, max_length=120, unique=False)
    quantity = models.IntegerField(negative=False, max=100, unique=False)


    def __str__(self):
        return self.name
