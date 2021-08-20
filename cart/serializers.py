from rest_framework import serializers

from .models import Cart, CartItem
from product.serializers import ProductCartSerializer


class CartItemSerializer(serializers.ModelSerializer):
	product = ProductCartSerializer()

	class Meta:
		model = CartItem
		fields = ('id', 'product', 'quantity')


class CartSerializer(serializers.ModelSerializer):
	products = serializers.SerializerMethodField()

	class Meta:
		model = Cart
		fields = ('id', 'user', 'get_products_quantity', 'get_cart_total', 'products')

	def get_products(self, instance):
		""" Retrieve products in the cart """
		cartitems =  instance.cartitem_set.all()
		serializer = CartItemSerializer(cartitems, many=True)
		return serializer.data


class GeneralCartSerializer(serializers.ModelSerializer):
	""" Serialize only brief info about cart """

	class Meta:
		model = Cart
		fields = ('id', 'user', 'get_products_quantity', 'get_cart_total')