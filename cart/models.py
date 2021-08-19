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
	updated = models.DateTimeField(auto_now=True)

	objects = CartManager()

	def __str__(self):
		return str(self.id)

	@property
	def get_products_quantity(self):
		""" Returns number of products in the cart """
		cartitems = self.cartitems_set.all()
		quantity = sum([item.quantity for item in cartitems])
		return quantity

	@property
	def get_cart_total(self):
		""" Returns total value of the products in the cart """
		cartitems = self.cartitems_set.all()
		total = sum([item.get_total_value for item in cartitems])
		return total


class CartItem(models.Model):
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=0)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.cart} {self.product}'

	@property
	def get_total_value(self):
		""" Returns total value of this product based on quantity """
		total = self.product.product_price * self.quantity
		return total
