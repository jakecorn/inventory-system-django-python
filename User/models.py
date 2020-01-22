from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.


class User(models.Model):
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=100)

	class Meta:
		db_table="user"
