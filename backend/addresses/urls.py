from rest_framework.routers import DefaultRouter

from addresses.views import AddressViewSet

router = DefaultRouter()
router.register('addresses', AddressViewSet)

urlpatterns = router.urls
