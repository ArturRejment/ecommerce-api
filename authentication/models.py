from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	email = models.CharField(max_length=255, unique=True)
	phone = models.CharField(max_length=255, unique=True)

	required_fields = ['first_name', 'last_name', 'email', 'phone']

	def __str__(self):
		return f'{self.first_name} {self.last_name}'



