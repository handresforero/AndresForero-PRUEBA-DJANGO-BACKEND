from rest_framework import viewsets, permissions
from .models import Pedido
from .serializers import PedidoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = PedidoSerializer