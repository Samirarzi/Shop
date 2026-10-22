from rest_framework import viewsets

from carts.models import Carts
from carts.serializers import CartsSerializer


class CartsViewSet(viewsets.ModelViewSet):
    queryset = Carts.objects.all()
    serializer_class = CartsSerializer
