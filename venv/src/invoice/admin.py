from django.contrib import admin
from .models import Invoice , invoice_link
# Register your models here.
admin.site.register(Invoice)
admin.site.register(invoice_link)