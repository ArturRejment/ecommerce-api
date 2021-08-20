from django.db import models


class Card(models.Model):
	brand = models.CharField(max_length=250, null=True, blank=True)
	country = models.CharField(max_length=250, null=True, blank=True)
	expiry_month = models.CharField(max_length=2)
	expiry_year = models.CharField(max_length=2)
	card_number = models.CharField(max_length=16)
	owners_first_name = models.CharField(max_length=250)
	owners_last_name = models.CharField(max_length=250)
	ccv_code = models.CharField(max_length=3)

	def __str__(self):
		return f'{self.brand} {self.get_last_4}'

	@property
	def get_last_4(self):
		""" Returns last 4 digits of the card number """
		return self.card_number[:-4]
