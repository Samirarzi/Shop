from rest_framework import serializers

from categories.models import Category


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
