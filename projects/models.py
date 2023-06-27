from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tecnology = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    celular = models.CharField(max_length=20)
    correo = models.EmailField()
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=50)


class Producto(models.Model):
    nombre = models.CharField(max_length=100)


class Pedido(models.Model):
    ESTADOS = (
        ('pendiente', 'Pendiente'),
        ('en ruta', 'En Ruta'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado')
    )
    REGLA_ENVIO = (
        ('domicilio', 'Domicilio'),
        ('recoge', 'Recoge en punto')
    )
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS)
    pagado = models.BooleanField(default=False)
    productos = models.ManyToManyField(Producto, through='DetallePedido')
    regla_envio = models.CharField(max_length=10, choices=REGLA_ENVIO)
    observaciones = models.TextField(blank=True)


class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
