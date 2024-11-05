from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=200)



class Moto(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    segunda_mano = models.BooleanField(default=False)
    caballos = models.IntegerField()
    votos_usuario = models.ManyToManyField(
                                           Cliente, 
                                           through='voto_cliente',
                                           related_name='voto',
                                           )
    

# modelo intermedio de la relacion manyToMany entre Cliente y moto para las votaciones
class Voto_cliente(models.Model):
    moto = models.ForeignKey(Moto, 
                             on_delete=models.CASCADE,
                             related_name='voto_moto'
                             )
    cliente = models.ForeignKey(Cliente,
                             on_delete=models.CASCADE,
                             related_name='voto_cliente'
                             )
    
    puntuacion=models.FloatField()
    comentario = models.TextField(max_length=200)
    fecha_voto = models.DateTimeField(timezone.now)


class Cuenta_bancaria(models.Model):
    numero_cuenta = models.CharField(max_length=100, unique=True)

    BANCOS=[('CA', 'Caixa'), ('BB', 'BBVA'), ('UN', 'Unicaja'), ('IN', 'ING')]
    banco= models.CharField(max_length=2, choices=BANCOS )

    cliente= models.OneToOneField(Cliente, 
                                  on_delete=models.CASCADE,
                                  related_name='cuenta_cliente'
                                  )







