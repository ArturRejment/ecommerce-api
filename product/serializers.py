from rest_framework import serializers

from .models import Product, Category, Season, Tag
from .relations import CategoryRelatedField


class CategorySerializer(serializers.ModelSerializer):

	class Meta:
		model = Category
		fields = (
			'category_name',
			'description',
		)


class SeasonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Season
		fields = (
			'name',
			'description',
		)


class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = (
			'name',
			'description',
		)


class ProductListSerializer(serializers.ModelSerializer):
	categories = CategoryRelatedField(many=True, required=False)

	class Meta:
		model = Product
		fields = (
			'id',
			'product_name',
			'retail_price_net',
			'categories',
			'image_url',
		)


class ProductDetailSerializer(serializers.ModelSerializer):
	categories = CategoryRelatedField(
		many=True,
		required=False,
	)

	class Meta:
		model = Product
		# TODO: Add seasons and tags to the fields
		fields = (
			'id',
			'product_name',
			'detail_description',
			'stock_status',
			'retail_price_net',
			'whole_price_net',
			'tax',
			'is_visible',
			'is_new',
			'accession_number',
			'shipping_cost',
			'categories',
		)


class ProductCartSerializer(serializers.ModelSerializer):

	class Meta:
		model = Product
		fields = (
			'id',
			'product_name',
			'retail_price_net',
			'image_url'
		)
