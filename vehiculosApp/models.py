from django.db import models
from conductoresApp.models import Conductor

# Create your models here.
class Vehiculo(models.Model):
    id = models.IntegerField(primary_key=True)    
    modelo = models.CharField('Modelo', max_length=4,null=False)
    placa = models.CharField('Placa',max_length=7, unique=True, null=False)
    capacidad = models.CharField('Capacidad',max_length=7, unique=False, null=True)
    conductor_id_3 = models.ForeignKey(Conductor, related_name='conductor_id_3', on_delete=models.CASCADE, null=True, blank=True, default="")
    
