from rest_framework import serializers
from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['price', 'discounted_price', 'state', 'user', 'address']
        read_only_fields = ['price', 'discounted_price', 'user', 'address', ]
