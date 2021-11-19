from django.db import models


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
	retail_price_net = models.DecimalField(
		verbose_name="Detaliczna cena netto [zł]",
		max_digits=10,
		decimal_places=4,
	)
	whole_price_whole = models.DecimalField(
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
	categories = models.ManyToManyField(
		to='product.Category',
		verbose_name="Kategorie",
		related_name='product_category',
	)
	product_picture = models.ImageField(
		upload_to='product_pictures',
		default='default.jpg',
		height_field=None,
		width_field=None,
		max_length=None,
	)

	class Meta:
		ordering = ('product_name',)

	@property
	def image_url(self):
		try:
			url = 'http://127.0.0.1:8000/static' + self.product_picture.url
		except Exception:
			url = ''
		return url

	def __str__(self):
		return f'{self.product_name} {self.product_price}zl'


class Category(models.Model):
	category_name = models.CharField(
		verbose_name="Nazwa kategorii",
		max_length=50,
		unique=True,
		blank=False,
		null=False,
	)

	def __str__(self):
		return self.category_name


class Image(models.Model):
	product_id = models.ForeignKey(
		to=Product,
		on_delete=models.CASCADE,
	)
	position = models.IntegerField()
	created_at = models.DateTimeField(
		auto_now_add=True,
	)
	updated_at = models.DateTimeField(
		auto_now=True,
	)
	src = models.ImageField(
		upload_to='product_products',
		default='default.jpg',
		height_field=None,
		width_field=None,
		max_length=None,
	)
	width = models.PositiveIntegerField()
	height = models.PositiveIntegerField()