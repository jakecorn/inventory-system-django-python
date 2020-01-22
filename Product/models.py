from django.db import models
from django.core.validators import MaxValueValidator
from django.forms import ModelForm,NumberInput,Select,TextInput
from Dealer.models import Dealer


class Supplier(models.Model):
	code = models.CharField(max_length=100,unique=True)
	name = models.CharField(max_length=100)
	number = models.IntegerField(blank=True)
	address = models.CharField(max_length=100,blank=True)

	class Meta:
		db_table="supplier"

	def __str__(self):
		return self.code+ " " +self.name

class Product(models.Model):
	product_code = models.CharField(max_length=100,unique=True)
	product_name = models.CharField(max_length=100)
	product_price = models.FloatField()
	product_discount = models.FloatField(default=0)
	product_quantity = models.IntegerField(null=False)
	supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE,null=True)

	class Meta:
		db_table="product"

	def __str__(self):
		return self.product_code+ " " +self.product_name


class ProductForm(ModelForm):

	class Meta:
		model = Product
		fields = '__all__'
		error_css_class="error"
		required_css_class="text-danger"
		labels={
			"product_discount":"Product Discount (%)"
		}
		widgets = {
			'product_code':TextInput(attrs={"class":"form-control"}),
			'product_name':TextInput(attrs={"class":"form-control"}),
			'product_price':NumberInput(attrs={"class":"form-control"}),
			'product_discount':NumberInput(attrs={"class":"form-control"}),
			'product_quantity':NumberInput(attrs={"class":"form-control","required":"True"}),
			'supplier':Select(attrs={"class":"form-control"}),
		}

class SupplierForm(ModelForm):

	class Meta:
		model = Supplier
		fields = '__all__'
		widgets = {
			'name':TextInput(attrs={"class":"form-control","required":"True"}),
			'code':TextInput(attrs={"class":"form-control"}),
			'number':NumberInput(attrs={"class":"form-control"}),
			'address':TextInput(attrs={"class":"form-control"}),
		}

class Inventory(models.Model):
	product = models.ForeignKey(Product)
	date = models.DateField()
	product_price = models.FloatField()
	product_discount = models.FloatField(default=0)
	product_quantity = models.IntegerField()
	dealer = models.ForeignKey(Dealer,on_delete=models.CASCADE,null=True)

	class Meta:
		db_table="inventory"

	@property
	def payment_with_discount(self):
		total = (self.product_price *self.product_quantity) -  ((self.product_price *self.product_quantity) * (self.product_discount/100))
		return  '{:0,.2f}'.format(total)