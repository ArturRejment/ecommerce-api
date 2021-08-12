from django.db import models


class Product(models.Model):
	product_name = models.CharField(max_length=255, blank=False, null=False)
	product_price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
	detail_description = models.TextField(blank=True, null=True)
	availability = models.PositiveIntegerField(null=True)
	accession_number = models.CharField(max_length=50)
	product_condition = models.CharField(max_length=50)
	shipping_cost = models.DecimalField(max_digits=7, decimal_places=2)
	categories = models.ManyToManyField('product.Category', related_name='product_category')

	def __str__(self):
		return f'{self.product_name} {self.product_price}zl'


class Category(models.Model):
	category_name = models.CharField(max_length=50, unique=True, null=False, blank=False)

	def __str__(self):
		return self.category_name