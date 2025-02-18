from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from controle_pedidos.views import ClienteViewSet, PedidoViewSet, ItemPedidoViewSet


router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'itens-do-pedido', ItemPedidoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]