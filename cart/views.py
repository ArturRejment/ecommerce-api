from typing import TYPE_CHECKING

from rest_framework import viewsets, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.decorators import action

from .serializers import CartSerializer, GeneralCartSerializer
from .models import Cart, CartItem
from product.models import Product

if TYPE_CHECKING:
	from django.http import HttpRequest
	from typing import Tuple


class CartView(viewsets.ViewSet):
	serializer_class = CartSerializer

	@staticmethod
	def get_objects(request: HttpRequest, pk: int) -> Tuple[Cart, CartItem]:
		""" Obtain necessary objects to manage the Cart """
		user = request.user

		if user is None:
			raise NotFound('Unauthenticated user cannot have cart')

		try:
			product = Product.objects.get(pk=pk)
		except Product.DoesNotExist:
			raise NotFound(f"Product with id {pk} does not exist")

		cart = Cart.objects.new_or_get(user=user)
		cart_item = CartItem.objects.get_or_create(cart=cart, product=product)
		return cart, cart_item

	def get_permissions(self):
		if self.action in ('get_cart',):
			# TODO: Change permission to IsAuthenticated
			self.permission_classes = AllowAny
		return super(CartView, self).get_permissions()

	@action(methods=['GET'], url_path='get', detail=True)
	def get_cart(self, request: HttpRequest, **kwargs):
		""" Retrieve cart for specific user. """
		user = request.user
		if user is None:
			raise NotFound('Unauthenticated user cannot have cart')
		# Retrieve cart for specific user
		cart = Cart.objects.new_or_get(user=user)
		serializer = self.serializer_class(cart)
		return Response(serializer.data, status.HTTP_200_OK)

	@action(methods=['POST'], url_path='add', detail=True)
	def add_product_to_cart(self, request: HttpRequest, pk: int = None):
		try:
			product = Product.objects.get(pk=pk)
		except Product.DoesNotExist:
			raise NotFound(f"Product with id '{pk}' does not exist.")
		# TODO: square this action away


class ManageCartItems(APIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = GeneralCartSerializer

	def get_objects(self, request, **kwargs):
		""" Obtain necessary objects to manage cart """
		user = request.user
		if user is None or not user.is_authenticated:
			raise NotFound('Unauthenticated user cannot add product to the cart')
		product_id = kwargs['id']
		try:
			product = Product.objects.get(id = product_id)
		except Product.DoesNotExist:
			raise NotFound('Cannot found this product')
		self.cart = Cart.objects.new_or_get(user = user)
		self.cartitem, created = CartItem.objects.get_or_create(cart=self.cart, product=product)

	def post(self, request, **kwargs):
		""" Add product specified by id to the cart """
		# Still in progress
		self.get_objects(request, **kwargs)
		self.cartitem.quantity = (self.cartitem.quantity + 1)
		self.cartitem.save()
		serializer = self.serializer_class(self.cart)
		return Response(serializer.data, status=200)

	def delete(self, request, **kwargs):
		""" Remove product specified by id from the cart """
		# Still in progress
		self.get_objects(request, **kwargs)
		self.cartitem.quantity = (self.cartitem.quantity - 1)
		if self.cartitem.quantity <= 0:
			self.cartitem.delete()
		else:
			self.cartitem.save()
		serializer = self.serializer_class(self.cart)
		return Response(serializer.data)
