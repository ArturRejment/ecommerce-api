from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .serializers import ProductListSerializer, ProductDetailSerializer
from .models import Product

class ProductListView(generics.ListAPIView):
	serializer_class = ProductListSerializer
	queryset = Product.objects.prefetch_related('categories')