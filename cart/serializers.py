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
		orderitems =  instance.cartitems_set.all()
		serializer = CartItemSerializer(orderitems, many=True)
		return serializer.data