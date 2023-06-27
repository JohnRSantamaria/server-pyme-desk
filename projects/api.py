from .models import Cliente, Producto, Pedido, DetallePedido
from .serializers import ClienteSerializer, ProductoSerializer, PedidoSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count, Sum, F
from datetime import datetime, timedelta


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClienteSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializer

    def create(self, request, *args, **kwargs):
        # Verificar si el producto ya existe
        nombre_producto = request.data.get('nombre')
        if Producto.objects.filter(nombre=nombre_producto).exists():
            return Response({'mensaje': 'Un producto con este nombre ya existe'}, status=status.HTTP_400_BAD_REQUEST)

        # Si no existe, llamar al método create original
        return super(ProductoViewSet, self).create(request, *args, **kwargs)


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PedidoSerializer


class ResumenView(APIView):
    def get(self, request):
        # Número de pedidos
        num_pedidos = Pedido.objects.count()

        # Número de clientes
        num_clientes = Cliente.objects.count()

        # Ingresos del último mes
        fecha_un_mes_atras = datetime.now() - timedelta(days=30)
        ingresos_ultimo_mes = Pedido.objects.filter(fecha__gte=fecha_un_mes_atras, pagado=True).aggregate(
            total_ingresos=Sum('detallepedido__cantidad') * F('detallepedido__producto__precio'))['total_ingresos']

        # Ciudad con más pedidos
        ciudad_mas_pedidos = Pedido.objects.values('cliente__ciudad').annotate(
            total=Count('cliente__ciudad')).order_by('-total').first()

        # Producto más vendido
        producto_mas_vendido = DetallePedido.objects.values(
            'producto__nombre').annotate(total=Sum('cantidad')).order_by('-total').first()

        return Response({
            'numero_de_pedidos': num_pedidos,
            'numero_de_clientes': num_clientes,
            'ingresos_del_ultimo_mes': ingresos_ultimo_mes,
            'ciudad_con_mas_pedidos': ciudad_mas_pedidos,
            'producto_mas_vendido': producto_mas_vendido
        })
