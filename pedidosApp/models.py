from django.db import models
from conductoresApp.models import Conductor

# Create your models here.
class Pedido(models.Model):
    id = models.IntegerField(primary_key=True)
    tipo_pedido = models.CharField('Tipo', max_length=20)
    direccion = models.CharField('Direccion',max_length=50,null=False)
    conductor_id_2 = models.ForeignKey(Conductor, related_name='conductor_id_2', on_delete=models.CASCADE, null=False, blank=True, default="")