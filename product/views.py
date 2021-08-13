from rest_framework import generics, mixins, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .serializers import ProductListSerializer, ProductDetailSerializer
from .models import Product


class ProductListView(generics.ListAPIView):
	serializer_class = ProductListSerializer
	queryset = Product.objects.prefetch_related('categories')


class ProductDetailView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
	serializer_class = ProductDetailSerializer

	def get_queryset(self):
		super().get_queryset()

	def retrieve(self, request, *args, **kwargs):
		try:
			instance = Product.objects.get(id = kwargs['id'])
		except Product.DoesNotExist:
			raise NotFound('Product with this id was not found')
		serializer = self.serializer_class(instance)
		return Response(serializer.data)
