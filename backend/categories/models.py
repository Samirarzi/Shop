from django.db import models
from django.db.models.functions import Now


class Category(models.Model):
    class Meta:
        db_table = "categories"

    class Categories(models.TextChoices):
        TSHIRT = "tshirt", "T-Shirt"
        SHIRT = "shirt", "Shirt"
        HOODIE = "hoodie", "Hoodie"
        SWEATSHIRT = "sweatshirt", "Sweatshirt"
        SWEATER = "sweater", "Sweater"
        JACKET = "jacket", "Jacket"
        COAT = "coat", "Coat"
        JEAN = "jean", "Jean"
        TROUSER = "trouser", "Trouser"
        SHORT = "short", "Short"
        DRESS = "dress", "Dress"
        SKIRT = "skirt", "Skirt"
        ACTIVEWEAR = "activewear", "Activewear"
        UNDERWEAR = "underwear", "Underwear"
        SWIMWEAR = "swimwear", "Swimwear"
        SHOE = "shoe", "Shoe"
        ACCESSORY = "accessory", "Accessory"

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True, choices=Categories.choices, null=False, blank=False)
    created_at = models.DateTimeField(db_default=Now())
    updated_at = models.DateTimeField(db_default=Now())
    deleted_at = models.DateTimeField(null=True, blank=True)
