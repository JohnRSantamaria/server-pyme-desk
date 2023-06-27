from .models import Project, Cliente, Producto, Pedido, DetallePedido
from rest_framework import viewsets, permissions, generics
from .serializers import ProjectSerializer, ClienteSerializer, ProductoSerializer, PedidoSerializer, DetallePedidoSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClienteSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PedidoSerializer

# Agrega aquí las vistas adicionales para métricas, etc.
