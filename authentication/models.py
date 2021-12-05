from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
	"""
	Custom user model manager where email is the unique identifiers
	for authentication instead of usernames.
	"""

	def create_user(self, email, password, **extra_fields):
		"""
		Create and save a User with the given email and password.
		"""

		if not email:
			raise ValueError(_('The Email must be set'))
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, email, password, **extra_fields):
		"""
		Create and save a SuperUser with the given email and password.
		"""

		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_active', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError(_('Superuser must have is_staff=True.'))
		if extra_fields.get('is_superuser') is not True:
			raise ValueError(_('Superuser must have is_superuser=True.'))
		return self.create_user(email, password, **extra_fields)


class User(AbstractUser):

	first_name = models.CharField(
		verbose_name="Imię",
		max_length=255,
	)
	last_name = models.CharField(
		verbose_name="Nazwisko",
		max_length=255,
	)
	email = models.CharField(
		verbose_name="Email",
		max_length=255,
		unique=True,
	)
	phone = models.CharField(
		verbose_name="Nr Telefonu",
		max_length=255,
		unique=True,
		null=True,
		blank=True,
	)
	username = None

	REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']
	USERNAME_FIELD = 'email'

	objects = CustomUserManager()

	class Meta:
		verbose_name = "Użytkownik"
		verbose_name_plural = "Użytkownicy"

	def __str__(self):
		return f'{self.first_name} {self.last_name}'


class Address(models.Model):

	post_code = models.CharField(
		verbose_name="Kod pocztowy",
		max_length=50,
	)
	country = models.CharField(
		verbose_name="Państwo",
		max_length=100,
	)
	city = models.CharField(
		verbose_name="Miasto",
		max_length=100,
	)
	street = models.CharField(
		verbose_name="Ulica",
		max_length=100,
		null=True,
		blank=True,
	)

	class Meta:
		verbose_name = "Adres"
		verbose_name_plural = "Adresy"
