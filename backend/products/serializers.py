from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["gender", "category", "name", "size", "price", "color"]

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value
