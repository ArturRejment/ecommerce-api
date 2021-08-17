from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from .serializers import CartSerializer
from .models import Cart


class CartDetailView(RetrieveAPIView):
	serializer_class = CartSerializer

	def retrieve(self, request, **kwargs):
		""" Retrieve cart for specific user """
		cart_id = kwargs['id']
		try:
			cart = Cart.objects.get(id = cart_id)
		except Cart.DoesNotExist:
			raise NotFound('Cart with this id does not exist')

		serializer = self.serializer_class(cart)
		return Response(serializer.data, status=200)
