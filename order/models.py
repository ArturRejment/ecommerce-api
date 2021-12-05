from django.db import models

from cart.models import Cart
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

	total_cost_net = models.DecimalField(
		verbose_name="Całkowity koszt zamówienia",
		max_digits=10,
		decimal_places=4,
	)
	discount_code = models.CharField(
		verbose_name="Kod rabatowy",
		max_length=50,
		null=True,
		blank=True,
	)
	status = models.PositiveSmallIntegerField(
		verbose_name="Status",
		choices=STATUS_CHOICE,
		default=0,
	)
	cart = models.OneToOneField(
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
