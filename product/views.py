from __future__ import annotations

from typing import TYPE_CHECKING

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework import status

from django.shortcuts import get_object_or_404

from .serializers import ProductDetailSerializer, ProductListSerializer
from .models import Product

if TYPE_CHECKING:
	from django.http import HttpRequest


class ProductViewSet(viewsets.GenericViewSet):
	queryset = Product.objects.all()
	permission_classes = (IsAuthenticated,)

	def get_permissions(self):
		if self.action in ('get_product', 'get_all_products',):
			self.permission_classes = (AllowAny,)
		return super(ProductViewSet, self).get_permissions()

	def get_serializer_class(self):
		if self.action in ('get_product',):
			self.serializer_class = ProductDetailSerializer
		elif self.action in ('get_all_products',):
			self.serializer_class = ProductListSerializer
		return super(ProductViewSet, self).get_serializer_class()

	@action(methods=['GET'], url_path='get', detail=True)
	def get_product(self, request: HttpRequest, *args, **kwargs) -> Response:
		product = get_object_or_404(self.queryset, pk=kwargs.get('pk'))
		serializer = self.get_serializer_class()
		serializer = serializer(product)
		return Response(serializer.data, status.HTTP_200_OK)

	@action(methods=['GET'], url_path='get-all', detail=False)
	def get_all_products(self, request: HttpRequest) -> Response:
		serializer = self.get_serializer_class()
		serializer = serializer(self.queryset, many=True)
		return Response(serializer.data, status.HTTP_200_OK)
