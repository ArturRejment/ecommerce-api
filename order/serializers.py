from rest_framework import serializers

from .models import Order
from cart.serializers import CartSerializer
from product.serializers import DiscountSerializer


class OrderSerializer(serializers.ModelSerializer):
    cart = CartSerializer()
    discount_code = DiscountSerializer()
    status = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = (
            'order_number',
            'total_cost_net',
            'discount_code',
            'status',
            'cart',
            'user',
        )

    def get_status(self, obj):
        return obj.get_status_display()