from rest_framework import serializers

from .models import Cart
from product.serializers import ProductCartSerializer


class CartSerializer(serializers.ModelSerializer):
	products = ProductCartSerializer(many=True)

	class Meta:
		model = Cart
		fields = ('id', 'user', 'products')