from rest_framework import serializers

from .models import Product, Category
from .relations import CategoryRelatedField


class ProductListSerializer(serializers.ModelSerializer):
	categories = CategoryRelatedField(many=True, required=False)

	class Meta:
		model = Product
		fields = ('product_name', 'product_price', 'categories')


class ProductDetailSerializer(serializers.ModelSerializer):
	categories = CategoryRelatedField(many=True, required=False)

	class Meta:
		model = Product
		fields = ('product_name', 'product_price', 'detail_description',
				  'availability', 'accession_number', 'product_condition',
				  'shipping_cost', 'categories')