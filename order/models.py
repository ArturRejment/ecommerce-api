import uuid

from django.db import models

from cart.models import Cart
from product.models import Discount
from authentication.models import User


class Order(models.Model):
	STATUS_CHOICE = (
		(0, "Nieopłacone"),
		(10, "Opłacone"),
		(20, "W realizacji"),
		(30, "Wysłane"),
		(40, "Gotowe do odbioru"),
		(50, "Dostarczone"),
	)

	class Meta:
		verbose_name = "Zamówienie"
		verbose_name_plural = "Zamówienia"

	order_number = models.UUIDField(
		default=uuid.uuid4,
		editable=False,
	)
	total_cost_net = models.DecimalField(
		verbose_name="Całkowity koszt zamówienia",
		max_digits=10,
		decimal_places=4,
	)
	discount_code = models.ForeignKey(
		to=Discount,
		on_delete=models.SET_NULL,
		verbose_name="Kod rabatowy",
		null=True,
		blank=True,
	)
	status = models.PositiveSmallIntegerField(
		verbose_name="Status",
		choices=STATUS_CHOICE,
		default=0,
	)
	cart = models.ForeignKey(
		to=Cart,
		verbose_name="Koszyk",
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
	)
	user = models.ForeignKey(
		to=User,
		verbose_name="Użytkownik",
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
	)
