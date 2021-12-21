from __future__ import annotations

from typing import TYPE_CHECKING

from django.shortcuts import get_object_or_404
from django.db.models import Q

from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework import status

from .serializers import (
	ProductDetailSerializer, ProductListSerializer, CategorySerializer, SeasonSerializer, TagSerializer
)
from .models import Product, Category, Tag, Season

if TYPE_CHECKING:
	from django.http import HttpRequest
	from django.db.models import QuerySet


class ProductViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
	queryset = Product.objects.all()
	permission_classes = (IsAuthenticated,)

	def get_queryset(self) -> QuerySet[Product]:
		"""Filter queryset."""
		queryset = self.queryset
		category = self.request.query_params.get('category', None)
		season = self.request.query_params.get('season', None)
		tag = self.request.query_params.get('tag', None)
		if tag is not None:
			queryset = queryset.filter(Q(tags__name=tag))
		if category is not None:
			queryset = queryset.filter(Q(categories__category_name=category))
		if season is not None:
			queryset = queryset.filter(Q(seasons__name=season))
		return queryset

	def get_permissions(self) -> list:
		if self.action in ('get_product', 'get_all_products',):
			self.permission_classes = [AllowAny]
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
		serializer = serializer(self.get_queryset(), many=True)
		return Response(serializer.data, status.HTTP_200_OK)


class ProductCrudViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductDetailSerializer
	permission_classes = (AllowAny,)


class CategoryCrudViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
	permission_classes = (AllowAny,)


class SeasonCrudViewSet(viewsets.ModelViewSet):
	queryset = Season.objects.all()
	serializer_class = SeasonSerializer
	permission_classes = (AllowAny,)


class TagCrudViewSerializer(viewsets.ModelViewSet):
	queryset = Tag.objects.all()
	serializer_class = TagSerializer
	permission_classes = (AllowAny,)
