from django.db import models
from apps.users.models import User
from apps.items.models import Items
# Create your models here.
class Cart(models.Model):
    belong_to = models.ForeignKey(User, related_name='cartOfUser', on_delete=models.CASCADE)
    item_list = models.ManyToManyField(Items, related_name='carts')
