from rest_framework import serializers

from carts.models import Carts


class CartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carts
        fields = ["user", "product"]
        read_only_fields = ["user",]
