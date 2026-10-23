from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from products.filters import ProductFilter
from products.models import Product
from products.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter