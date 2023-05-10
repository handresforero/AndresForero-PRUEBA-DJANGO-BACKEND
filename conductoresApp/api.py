from rest_framework import viewsets, permissions
from .models import Conductor
from .serializers import ConductorSerializer

class ConductorViewSet(viewsets.ModelViewSet):
    queryset = Conductor.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = ConductorSerializer