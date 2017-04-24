from django.db import models
from accounts.models import User
import datetime

class Invoice(models.Model):
    name = models.ForeignKey(User)
    total = models.FloatField()
    created_date = models.DateField(default=datetime.datetime.now())

    def __str__(self):
        return str(self.id)


class invoice_link(models.Model):
    invoice_id = models.ForeignKey(Invoice)
    product_name = models.CharField(max_length=40)
    quantity = models.PositiveIntegerField()
    price = models.FloatField()
    def __str__(self):
        return str(self.invoice_id)
