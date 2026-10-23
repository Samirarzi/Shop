from rest_framework import viewsets
from django_filters import DjangoFilterBackends

from products.filters import ProductFilter
from products.models import Product
from products.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackends]
    filterset_class = ProductFilter