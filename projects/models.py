from django.db import models

# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    celular = models.CharField(max_length=20)
    correo = models.EmailField()
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=50)


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(
        max_digits=10, decimal_places=2)  # Precio del producto


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

    @property
    def precio_total(self):
        return self.cantidad * self.producto.precio
