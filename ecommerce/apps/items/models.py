from django.db import models
from apps.users.models import User
# Create your models here.
class Items(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False, default='Items')
    des = models.TextField(null=False, blank=False, default='Item des')
    price = models.FloatField(null=False, default=0.0)
    sales_off = models.FloatField(null=False, default=0.0)

    create = models.DateField()
    update = models.DateField()

    belong_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='item')
    