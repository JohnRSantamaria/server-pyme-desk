from rest_framework.exceptions import APIException
from .models import Cliente, Producto, Pedido, DetallePedido
from .serializers import ClienteSerializer, ProductoSerializer, PedidoSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.db.models import Count, Sum, F, ExpressionWrapper, DecimalField
from datetime import datetime, timedelta
# filter
from django_filters.rest_framework import DjangoFilterBackend


class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClienteSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ciudad',]


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializer
    pagination_class = CustomPageNumberPagination

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
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'estado', 'pagado',
                        'regla_envio', 'cliente']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        # Itera sobre los pedidos serializados
        for pedido_data in serializer.data:
            # Obtén los IDs de productos y cliente del pedido actual
            productos_ids = [detalle['producto']
                             for detalle in pedido_data['productos']]
            cliente_id = pedido_data['cliente']

            # Obtén los nombres de los productos y el cliente asociado
            productos = Producto.objects.filter(id__in=productos_ids)
            cliente = Cliente.objects.get(id=cliente_id)

            # Agrega los nombres de los productos al pedido_data
            pedido_data['productos_nombres'] = [
                producto.nombre for producto in productos]

            # Agrega el nombre del cliente al pedido_data
            pedido_data['cliente_nombre'] = cliente.nombre

        return Response(serializer.data)


class ResumenView(APIView):
    def get(self, request):
        # Número de pedidos
        num_pedidos = Pedido.objects.count()

        # Número de clientes
        num_clientes = Cliente.objects.count()

        # Ingresos del último mes
        fecha_un_mes_atras = datetime.now() - timedelta(days=30)

        # Ingresos del último mes
        fecha_un_mes_atras = datetime.now() - timedelta(days=30)
        detalle_pedidos = DetallePedido.objects.filter(
            pedido__fecha__gte=fecha_un_mes_atras,
            pedido__pagado=True
        )
        ingresos_ultimo_mes = detalle_pedidos.aggregate(
            total_ingresos=Sum(F('cantidad') * F('producto__precio'))
        )['total_ingresos']

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
