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
        extra_kwargs = {
            'pedido': {'write_only': True, 'required': False}
        }


class PedidoSerializer(serializers.ModelSerializer):
    # productos = DetallePedidoSerializer(many=True, write_only=True)
    productos = DetallePedidoSerializer(
        source='detallepedido_set', many=True, read_only=True)

    class Meta:
        model = Pedido
        fields = '__all__'

    def create(self, validated_data):
        productos_data = validated_data.pop('productos', [])
        pedido = Pedido.objects.create(**validated_data)
        for producto_data in productos_data:
            DetallePedido.objects.create(pedido=pedido, **producto_data)
        return pedido
