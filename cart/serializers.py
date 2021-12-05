from rest_framework import serializers

from .models import Cart, CartItem
from product.serializers import ProductCartSerializer


class CartItemSerializer(serializers.ModelSerializer):
	product = ProductCartSerializer()

	class Meta:
		model = CartItem
		fields = (
			'id',
			'product',
			'quantity',
		)


class CartSerializer(serializers.ModelSerializer):
	products = serializers.SerializerMethodField(method_name='get_products')

	class Meta:
		model = Cart
		fields = (
			'id',
			'user',
			'get_products_quantity',
			'get_cart_total',
			'products'
		)

	@staticmethod
	def get_products(instance: Cart):
		""" Retrieve products in the cart """
		cart_items = instance.cartitem_set.all()
		serializer = CartItemSerializer(cart_items, many=True)
		return serializer.data


class GeneralCartSerializer(serializers.ModelSerializer):
	""" Serialize only brief info about cart """

	class Meta:
		model = Cart
		fields = (
			'id',
			'user',
			'get_products_quantity',
			'get_cart_total',
		)
