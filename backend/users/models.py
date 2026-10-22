from django.db import models
from django.db.models.functions import Now


class User(models.Model):
    class Role(models.TextChoices):
        USER = 'user', 'User',
        ADMIN = 'admin', 'Admin'

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=Role.choices)
    created_at = models.DateTimeField(db_default=Now())
    updated_at = models.DateTimeField(db_default=Now())
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'users'
