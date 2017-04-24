from django.db import models
from accounts.models import User
# Create your models here.

CONTACT_TYPE = (
    ('custumer', 'custumer'),
    ('vendor','vendor')
)
class contacts(models.Model):
    user = models.ForeignKey(User)#replace user with uid
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    company_name = models.CharField(max_length=20, blank=True , null=True)
    email = models.CharField(max_length=20, blank=True, null=True)
    phone = models.PositiveIntegerField(null=True , blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    contact_type = models.CharField(max_length=10,choices=CONTACT_TYPE, null=True , blank=True )
    def __str__(self):
        return str(self.id)
