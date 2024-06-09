from django.db import models
from apps.items.models import Items
from .enum import CatType
# Create your models here.
class Category(models.Model):
    category = models.ManyToManyField(Items, related_name='catItems')
    name = models.CharField(CatType.choices(), blank=False, null = False,default=CatType.TECH.value, max_length=20)