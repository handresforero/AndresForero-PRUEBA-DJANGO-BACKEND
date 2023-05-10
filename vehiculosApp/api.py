from rest_framework import viewsets, permissions
from .models import Vehiculo
from .serializers import VehiculoSerializer

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = VehiculoSerializer