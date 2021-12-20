from __future__ import annotations

from typing import TYPE_CHECKING

from django.db import models

if TYPE_CHECKING:
	from decimal import Decimal


class Product(models.Model):
	STOCK_STATUS_CHOICE = (
		(0, "Brak"),
		(10, "Ostatnie sztuki"),
		(20, "Dostępne"),
	)

	product_name = models.CharField(
		verbose_name="Nazwa produktu",
		max_length=255,
	)
	detail_description = models.TextField(
		verbose_name="Opis",
		null=True,
		blank=True,
	)
	stock_status = models.PositiveIntegerField(
		verbose_name="Dostępność",
		choices=STOCK_STATUS_CHOICE,
	)
	stock_availability = models.PositiveIntegerField(
		verbose_name="Stan magazynowy",
		default=0,
	)
	retail_price_net = models.DecimalField(
		verbose_name="Detaliczna cena netto [zł]",
		max_digits=10,
		decimal_places=4,
	)
	whole_price_net = models.DecimalField(
		verbose_name="Hurtowa cena netto [zł]",
		max_digits=10,
		decimal_places=4,
	)
	tax = models.DecimalField(
		verbose_name="Podatek VAT [%]",
		max_digits=10,
		decimal_places=4,
	)
	is_visible = models.BooleanField(
		verbose_name="Czy widoczny",
		default=True,
	)
	is_new = models.BooleanField(
		verbose_name="Czy nowy",
		default=True,
	)
	accession_number = models.CharField(
		verbose_name="Numer katalogowy",
		max_length=50,
		null=True,
		blank=True,
	)
	shipping_cost = models.DecimalField(
		verbose_name="Cena dostawy",
		max_digits=7,
		decimal_places=2,
		blank=True,
		null=True,
	)
	product_picture = models.ImageField(
		upload_to='product_pictures',
		default='default.jpg',
		height_field=None,
		width_field=None,
		max_length=None,
		null=True,
		blank=True,
	)
	categories = models.ManyToManyField(
		to='product.Category',
		verbose_name="Kategorie",
		related_name='product_category',
	)
	seasons = models.ManyToManyField(
		to='Season',
		verbose_name="Sezony",
		related_name='season_category',
	)
	tags = models.ManyToManyField(
		to='Tag',
		verbose_name="Tagi",
		related_name='product_tags',
	)

	class Meta:
		verbose_name = "Produkt"
		verbose_name_plural = "Produkty"
		ordering = ('product_name',)

	@property
	def image_url(self):
		url = ''
		if self.product_picture.url:
			url = 'http://127.0.0.1:8000/static' + self.product_picture.url
		return url

	@property
	def whole_price_brutt(self) -> Decimal:
		return self.whole_price_net * (1+self.tax/100)

	@property
	def retail_price_brutt(self) -> Decimal:
		return self.retail_price_net * (1+self.tax/100)

	def __str__(self):
		return f'{self.product_name}'


class Category(models.Model):
	category_name = models.CharField(
		verbose_name="Nazwa kategorii",
		max_length=100,
		unique=True,
	)
	description = models.TextField(
		verbose_name="Opis",
		null=True,
		blank=True,
	)

	class Meta:
		verbose_name = "Kategoria"
		verbose_name_plural = "Kategorie"

	def __str__(self):
		return self.category_name


class Season(models.Model):
	name = models.CharField(
		verbose_name="Nazwa sezonu",
		max_length=100,
		unique=True,
	)
	description = models.TextField(
		verbose_name="Opis",
		null=True,
		blank=True,
	)

	class Meta:
		verbose_name = "Sezon"
		verbose_name_plural = "Sezony"

	def __str__(self):
		return self.name


class Tag(models.Model):
	name = models.CharField(
		verbose_name="Nazwa",
		max_length=100,
		unique=True,
	)
	description = models.TextField(
		verbose_name="Opis",
		null=True,
		blank=True,
	)

	class Meta:
		verbose_name = "Tag"
		verbose_name_plural = "Tagi"

	def __str__(self):
		return self.name


class Discount(models.Model):
	code = models.CharField(
		verbose_name="Kod rabatowy",
		max_length=100,
		unique=True,
	)
	percentage_value = models.PositiveIntegerField(
		verbose_name="Wartość procentowa",
	)
	is_disposable = models.BooleanField(
		verbose_name="Czy jednorazowy",
		default=True,
	)

	class Meta:
		verbose_name = "Zniżka"
		verbose_name_plural = "Zniżki"

	def __str__(self):
		return self.code
