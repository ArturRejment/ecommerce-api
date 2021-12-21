from __future__ import annotations

from typing import TYPE_CHECKING

from rest_framework import viewsets, status
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from .serializers import CartSerializer
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
		cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
		return cart, cart_item

	def get_permissions(self) -> list:
		if self.action in ('get_cart', 'add_product_to_cart', 'remove_product_from_cart'):
			self.permission_classes = (IsAuthenticated,)
		return super(CartView, self).get_permissions()

	@action(methods=['GET'], url_path='get', detail=False)
	def get_cart(self, request: HttpRequest) -> Response:
		""" Retrieve cart for specific user. """
		user = request.user
		if user is None:
			raise NotFound('Unauthenticated user cannot have cart')
		# Retrieve cart for specific user
		cart = Cart.objects.new_or_get(user=user)
		serializer = self.serializer_class(cart)
		return Response(serializer.data, status.HTTP_200_OK)

	@action(methods=['POST'], url_path='add', detail=True)
	def add_product_to_cart(self, request: HttpRequest, pk: int = None) -> Response:
		cart, cart_item = self.get_objects(request, pk)
		cart_item.quantity = (cart_item.quantity + 1)
		if cart_item.quantity > cart_item.product.stock_availability:
			raise ValidationError("No more products are available is stock")
		cart_item.save()
		serializer = self.serializer_class(cart)
		return Response(serializer.data, status.HTTP_200_OK)

	@action(methods=['POST'], url_path='remove', detail=True)
	def remove_product_from_cart(self, request: HttpRequest, pk: int = None) -> Response:
		cart, cart_item = self.get_objects(request, pk)
		cart_item.quantity = (cart_item.quantity - 1)
		if cart_item.quantity <= 0:
			cart_item.delete()
		else:
			cart_item.save()
		serializer = self.serializer_class(cart)
		return Response(serializer.data, status.HTTP_200_OK)
