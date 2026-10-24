from django.db import models
from django.db.models.functions import Now

from products.models import Product
from users.models import User


class Carts(models.Model):
    class Meta:
        db_table = "carts"


    user= models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(db_default=Now())
    updated_at = models.DateTimeField(db_default=Now())
    deleted_at = models.DateTimeField(null=True, blank=True)
