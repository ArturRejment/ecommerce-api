from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .serializers import CartSerializer
from .models import Cart, CartItems
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
	serializer_class = ProductDetailSerializer

	def post(self, request, **kwargs):
		""" Add product specified by id to the cart """
		# Still in progress
		user = request.user
		if user is None or not user.is_authenticated:
			raise NotFound('Unauthenticated user cannot add product to the cart')
		product_id = kwargs['id']
		try:
			product = Product.objects.get(id = product_id)
		except Product.DoesNotExist:
			raise NotFound('Cannot found this product')
		cart = Cart.objects.new_or_get(user = user)
		cartitem, created = CartItems.objects.get_or_create(cart=cart, product=product)
		cartitem.quantity = (cartitem.quantity + 1)
		cartitem.save()
		return Response({'product':'created'})
