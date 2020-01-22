from django import forms
from django.core.validators import MaxValueValidator

class ProductForm(forms.Form):
	product_code = forms.CharField(max_length=100)
	product_name = forms.CharField(max_length=5)
	product_price = forms.IntegerField()
	product_quantity = forms.IntegerField()
