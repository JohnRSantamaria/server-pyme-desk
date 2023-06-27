from rest_framework.routers import DefaultRouter
from .api import ProjectViewSet, ClienteViewSet, ProductoViewSet, PedidoViewSet

router = DefaultRouter()
router.register('api/projects', ProjectViewSet, 'projects')
router.register('api/clientes', ClienteViewSet, 'clientes')
router.register('api/productos', ProductoViewSet, 'productos')
router.register('api/pedidos', PedidoViewSet, 'pedidos')

urlpatterns = router.urls
