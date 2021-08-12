from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .serializers import ProductSerializer
from .models import Product

class ProductListView(generics.ListAPIView):
	serializer_class = ProductSerializer
	queryset = Product.objects.prefetch_related('categories')