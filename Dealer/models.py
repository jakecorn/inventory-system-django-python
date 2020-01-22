from django.db import models
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm,TextInput,CharField,NumberInput
from django.core.validators import MinLengthValidator
# Create your models here.

class Dealer(models.Model):
	dealer_name 			= models.CharField(max_length=100, null=False,help_text="Dealer Name")
	dealer_address 			= models.CharField(max_length=20, null=False)
	dealer_contact_number 	= models.CharField(max_length=20)
	dealer_email 			= models.EmailField(blank=True)

	class Meta:
		db_table = "dealer"

	def __str__(self):
		return self.dealer_name



class DealerForm(ModelForm):
	class Meta:
		model = Dealer
		# fields = '__all__' #to include all the fields in the form

		fields = ['dealer_name','dealer_address','dealer_email','dealer_contact_number'] #specify what fields to be included in the form
		
		widgets = {
			'dealer_name': TextInput(attrs={'class':'form-control'}),
			'dealer_address': TextInput(attrs={'class':'form-control'}),
			'dealer_email': TextInput(attrs={'class':'form-control'}),
			'dealer_contact_number': NumberInput(attrs={'class':'form-control'}),
		}

		labels = {
			'dealer_name':_("Dealer Name"),
			'dealer_contact_number':_("Contact Number"),
		}

		# help_text ={
		# 	'dealer_name':_("Input the correct dealer name"),
		# 	'dealer_contact_number':_("Contact number must a Globe network"),
		# }

		# error_message ={
		# 	'dealer_address':{
		# 		'max_length':_("Address must not exceed 20 characters"),
		# 	}
		# }

		# validators = {
		# 	'dealer_address': MinLengthValidator(2)
		# }

class Payment(models.Model):
	dealer 		= models.ForeignKey(Dealer)
	date 		= models.DateField()
	date_paid 		= models.DateField()
	amount 		= models.FloatField()

