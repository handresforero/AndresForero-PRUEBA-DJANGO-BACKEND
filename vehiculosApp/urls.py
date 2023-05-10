from rest_framework import routers
from .api import VehiculoViewSet
router = routers.DefaultRouter()
router.register('api/vehiculo', VehiculoViewSet, 'vehiculo')

urlpatterns = router.urls

