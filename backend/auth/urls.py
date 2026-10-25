from django.urls import path

from auth.views import LoginAPIView, RefreshAPIView

urlpatterns = [
    path("login", LoginAPIView().as_view(), name="login"),
    path('refresh', RefreshAPIView().as_view(), name="refresh"),
]
