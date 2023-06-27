from .models import Cliente, Producto, Pedido, DetallePedido
from rest_framework import serializers


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


class DetallePedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = '__all__'
        read_only_fields = ('fecha')


class PedidoSerializer(serializers.ModelSerializer):
    productos = DetallePedidoSerializer(source='detallepedido_set', many=True)

    class Meta:
        model = Pedido
        fields = '__all__'
