from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import CartSerializer
from .models import Cart


class CartDetailView(RetrieveAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = CartSerializer

	def retrieve(self, request):
		""" Retrieve cart for specific user """
		user = request.user
		if user is None or not user.is_authenticated:
			raise NotFound('Unauthenticated user cannot have cart')

		cart = Cart.objects.new_or_get(user = user)

		serializer = self.serializer_class(cart)
		return Response(serializer.data, status=200)
