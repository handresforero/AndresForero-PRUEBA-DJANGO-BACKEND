from rest_framework import routers
from .api import PedidoViewSet
router = routers.DefaultRouter()
router.register('api/pedidos', PedidoViewSet, 'pedidos')

urlpatterns = router.urls

