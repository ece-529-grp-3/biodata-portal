from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import BiodataViewSet

router = SimpleRouter()
router.register('biodata', BiodataViewSet, basename='biodata')

urlpatterns = router.urls