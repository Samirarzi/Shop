from django.urls import path, include

urlpatterns = [
    path("api/v1/", include('categories.urls')),
    path("api/v1/", include('products.urls')),
    path("api/v1/", include('users.urls')),
]
