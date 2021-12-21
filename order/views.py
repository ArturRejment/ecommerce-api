from __future__ import annotations

from typing import TYPE_CHECKING

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.response import Response

from .models import Order
from cart.models import Cart
from product.models import Discount
from .serializers import OrderSerializer
from product.utils import generate_discount_code
from product.serializers import DiscountSerializer

if TYPE_CHECKING:
    from django.http import HttpRequest


class OrderViewSet(viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)

    @action(methods=['POST'], url_path='create', detail=False)
    def create_order(self, request: HttpRequest, *args, **kwargs):
        cart = Cart.objects.new_or_get(user=request.user)
        if not cart.is_valid_cart():
            raise ValidationError("There is an issue with your cart. Please, contact us for help.")
        discount = None
        total_cart_value = cart.get_cart_total
        try:
            code = request.data.get('discount_code', None)
            discount = Discount.objects.get(code=code)
        except Discount.DoesNotExist:
            raise NotFound("Please, enter valid discount code.")

        if discount.is_disposable and discount.is_used:
            raise ValidationError("This code is already used.")

        order = Order.objects.create(
            cart=cart,
            status=0,
            total_cost_net=total_cart_value,
            user=request.user,
            discount_code=discount,
        )
        order.save()
        new_discount = generate_discount_code()
        serializer = DiscountSerializer(new_discount)
        return Response(serializer.data)

