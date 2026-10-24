from rest_framework import serializers

from carts.models import Carts


class CartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carts
        fields = ["user", "product", "quantity", "user",]
        # read_only_fields = ["user", ]

        def validate_quantity(self, value):
            if value < 0:
                raise serializers.ValidationError("Quantity must be greater than zero.")
            return value
