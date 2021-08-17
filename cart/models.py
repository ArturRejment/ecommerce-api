from django.db import models
from django.conf import settings
from rest_framework.exceptions import NotFound

from product.models import Product

User = settings.AUTH_USER_MODEL

class CartManager(models.Manager):

	def new_or_get(self, user):
		try:
			cart = self.model.objects.get(user = user.id)
		except Exception:
			cart = self.model.objects.new(user = user)
		return cart

	def new(self, user=None):
		if user is None or not user.is_authenticated:
			raise NotFound('User does not exist')
		return self.model.objects.create(user=user)


class Cart(models.Model):
	user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	products = models.ManyToManyField(Product, related_name='cart_products')
	total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	objects = CartManager()

	def __str__(self):
		return str(self.id)

