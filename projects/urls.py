from rest_framework.routers import DefaultRouter
from .api import ClienteViewSet, ProductoViewSet, PedidoViewSet, ResumenView
from django.urls import path

router = DefaultRouter()
router.register('api/clientes', ClienteViewSet, 'clientes')
router.register('api/productos', ProductoViewSet, 'productos')
router.register('api/pedidos', PedidoViewSet, 'pedidos')

urlpatterns = router.urls + [path('api/resumen/', ResumenView.as_view())]
