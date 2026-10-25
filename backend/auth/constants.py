from datetime import timedelta

from django.utils import timezone

REFRESH_TOKEN_EXPIRE_TIME = timezone.now() + timedelta(days=1)
ACCESS_TOKEN_EXPIRE_TIME = timezone.now() + timedelta(minutes=10)
