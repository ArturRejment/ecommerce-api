from rest_framework import serializers

from .models import Order
from cart.serializers import CartSerializer
from product.serializers import DiscountSerializer


class OrderSerializer(serializers.ModelSerializer):
    cart = CartSerializer()
    discount_code = DiscountSerializer()
    status = serializers.ChoiceField(choices=Order.STATUS_CHOICE)

    class Meta:
        model = Order
        fields = (
            'total_cost_net',
            'discount_code',
            'status',
            'cart',
            'user',
        )
