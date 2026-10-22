from rest_framework import viewsets

from categories.models import Category
from categories.serializers import CategorySerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
