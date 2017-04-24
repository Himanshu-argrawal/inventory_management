from django.db import models
from accounts.models import User
# Create your models here.

class product(models.Model):
    user = models.ForeignKey(User)#replace user with uid
    name = models.CharField(max_length=40 , null=True , blank=True)
    product_code = models.CharField(max_length=20 , blank=True , null=True , unique=True)
    product_cost = models.PositiveIntegerField(blank=True , null=True)
    product_detials = models.CharField(max_length=255 , null=True , blank=True)
    product_count = models.PositiveIntegerField(blank=True , null=True)
    product_sold = models.PositiveIntegerField(blank=True , null=True, default=0)
    product_add = models.PositiveIntegerField(blank=True , null=True)
    product_minstock = models.PositiveIntegerField(blank=True, null=True, default=0)
    tax_rate = models.IntegerField(blank=True , null=True)
    product_total = models.PositiveIntegerField(blank= True , null = True , default=0)
    product_sell = models.PositiveIntegerField(blank=True , null=True)
    tax_name = models.CharField(max_length=20 , null=True , blank=True)
    product_adjust =models.BooleanField(default=False)

    def __str__(self):
        return str(self.product_sell)


