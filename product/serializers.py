from rest_framework import serializers

from .models import Product, Category


class ProductSerializer(serializers.ModelSerializer):

	class Meta:
		model = Product
		fields = ('product_name', 'product_price', 'detail_description',
				  'availability', 'accession_number', 'product_condition',
				  'shipping_cost', 'categories')