from rest_framework.exceptions import NotFound

from django.db import models
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from product.models import Product

User = settings.AUTH_USER_MODEL


class CartManager(models.Manager):

	def new_or_get(self, user):
		try:
			cart = self.model.objects.get(user=user.id)
		except ObjectDoesNotExist:
			cart = self.model.objects.new(user=user)
		return cart

	def new(self, user=None):
		if user is None or not user.is_authenticated:
			raise NotFound('User does not exist')
		return self.model.objects.create(user=user)


class Cart(models.Model):
	user = models.ForeignKey(
		to=User,
		verbose_name="Użytkownik",
		on_delete=models.CASCADE,
		null=True,
		blank=True,
	)
	updated = models.DateTimeField(
		verbose_name="Data uaktualnienia",
		auto_now=True,
	)
	products = models.ManyToManyField(
		to=Product,
		verbose_name="Produkty w koszyku",
		through='CartItem',
	)

	objects = CartManager()

	def __str__(self):
		return str(self.id)

	@property
	def get_products_quantity(self):
		""" Returns number of products in the cart """
		cart_items = self.cartitem_set.all()
		quantity = sum([item.quantity for item in cart_items])
		return quantity

	@property
	def get_cart_total(self):
		""" Returns total value of the products in the cart """
		cart_items = self.cartitem_set.all()
		total = sum([item.get_total_value for item in cart_items])
		return total


class CartItem(models.Model):
	cart = models.ForeignKey(
		to=Cart,
		verbose_name="Koszyk",
		on_delete=models.CASCADE,
	)
	product = models.ForeignKey(
		to=Product,
		verbose_name="Produkt",
		on_delete=models.CASCADE,
	)
	quantity = models.IntegerField(
		verbose_name="Ilość w koszyku",
		default=0,
	)
	added_at = models.DateTimeField(
		auto_now_add=True,
	)

	def __str__(self):
		return f'{self.cart} {self.product}'

	@property
	def get_total_value(self):
		""" Returns total value of this product based on quantity """

		# If quantity is greater than 9, count total value with whole price
		if self.quantity >= 10:
			total = self.product.whole_price_whole * self.quantity
		else:
			total = self.product.retail_price_net * self.quantity
		return total
