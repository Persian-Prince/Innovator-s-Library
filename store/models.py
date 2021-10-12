from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    mrp = models.PositiveIntegerField(blank=True, null=True)
    rating = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MaxValueValidator(10), MinValueValidator(1)])
