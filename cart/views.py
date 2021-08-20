from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .serializers import CartSerializer, GeneralCartSerializer
from .models import Cart, CartItem
from product.serializers import ProductDetailSerializer
from product.models import Product


class CartDetailView(RetrieveAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = CartSerializer

	def retrieve(self, request):
		""" Retrieve cart for specific user """
		user = request.user
		if user is None or not user.is_authenticated:
			raise NotFound('Unauthenticated user cannot have cart')
		# Retrieve or create user's cart
		cart = Cart.objects.new_or_get(user = user)
		serializer = self.serializer_class(cart)
		return Response(serializer.data, status=200)


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
