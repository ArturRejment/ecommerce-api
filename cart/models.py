from django.db import models
from django.conf import settings

from product.models import Product

User = settings.AUTH_USER_MODEL


class Cart(models.Model):
	user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	products = models.ManyToManyField(Product, related_name='cart_products')
	total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.id)

