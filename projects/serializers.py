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


# class PedidoSerializer(serializers.ModelSerializer):
#     productos = DetallePedidoSerializer(
#         source='detallepedido_set', many=True, read_only=True)

#     class Meta:
#         model = Pedido
#         fields = '__all__'

#     def create(self, validated_data):
#         productos_data = validated_data.pop('productos', [])
#         pedido = Pedido.objects.create(**validated_data)
#         for producto_data in productos_data:
#             DetallePedido.objects.create(pedido=pedido, **producto_data)
#         return pedido
class PedidoSerializer(serializers.ModelSerializer):
    productos = DetallePedidoSerializer(
        source='detallepedido_set', many=True, read_only=True)

    class Meta:
        model = Pedido
        fields = '__all__'

    def create(self, validated_data):
        # Asumiendo que estás enviando los productos como parte de la petición POST
        # en un campo llamado 'productos_data'.
        productos_data = self.context['request'].data.get('productos', [])
        pedido = Pedido.objects.create(**validated_data)

        # Ahora, para cada producto en productos_data, crea un DetallePedido.
        for producto_data in productos_data:
            producto_id = producto_data.get('producto')
            cantidad = producto_data.get('cantidad')
            producto = Producto.objects.get(id=producto_id)
            DetallePedido.objects.create(
                pedido=pedido, producto=producto, cantidad=cantidad)

        return pedido
