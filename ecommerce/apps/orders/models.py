from django.db import models
from apps.users.models import User
from apps.items.models import Items
from django.utils import timezone
# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userOrder')
    items_list = models.ManyToManyField(Items, related_name='itemsOrder')

    date_record = models.DateField(timezone.now())
    total = models.FloatField(null= False, default=0.0)


