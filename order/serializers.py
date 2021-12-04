from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'total_cost_net',
            'discount_code',
            'status',
            'cart',
            'user',
        )
