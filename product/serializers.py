from rest_framework import serializers

from .models import Product, Category, Season, Tag
from .relations import CategoryRelatedField, TagRelatedField, SeasonRelatedField


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
			'retail_price_brutt',
			'categories',
			'image_url',
		)


class ProductDetailSerializer(serializers.ModelSerializer):
	categories = CategoryRelatedField(
		many=True,
		required=False,
	)
	tags = TagRelatedField(
		many=True,
		required=False,
	)
	seasons = SeasonRelatedField(
		many=True,
		required=False,
	)

	class Meta:
		model = Product
		fields = (
			'id',
			'product_name',
			'detail_description',
			'stock_status',
			'retail_price_brutt',
			'whole_price_brutt',
			'tax',
			'is_visible',
			'is_new',
			'accession_number',
			'shipping_cost',
			'categories',
			'tags',
			'seasons',
		)


class ProductCartSerializer(serializers.ModelSerializer):

	class Meta:
		model = Product
		fields = (
			'id',
			'product_name',
			'retail_price_brutt',
			'image_url'
		)
