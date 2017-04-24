from django import forms
from django.core.exceptions import ValidationError
from Product.models import product

class product_addform(forms.ModelForm):
    class Meta:
        model = product
        fields = ['name','product_code','product_cost','product_detials','product_count']

