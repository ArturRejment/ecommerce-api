from rest_framework import serializers

from .models import Product, Category, Season, Tag, Discount
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
	categories = CategoryRelatedField(
		many=True,
		required=False,
	)
	seasons = TagRelatedField(
		many=True,
		required=False,
	)
	tags = TagRelatedField(
		many=True,
		required=False,
	)
	stock_status = serializers.ChoiceField(
		choices=Product.STOCK_STATUS_CHOICE
	)

	class Meta:
		model = Product
		fields = (
			'id',
			'product_name',
			'retail_price_brutt',
			'stock_status',
			'stock_availability',
			'categories',
			'seasons',
			'tags',
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
			'image_url',
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


class DiscountSerializer(serializers.ModelSerializer):

	class Meta:
		model = Discount
		fields = (
			'code',
		)
