from rest_framework import routers
from .api import ConductorViewSet
router = routers.DefaultRouter()
router.register('api/conductor', ConductorViewSet, 'conductor')

urlpatterns = router.urls

