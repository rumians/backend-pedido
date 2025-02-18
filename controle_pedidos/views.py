from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import Cliente, Pedido, ItemPedido

from .serializers import ClienteSerializer, PedidoSerializer, ItemPedidoSerializer

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class ItemPedidoViewSet(ModelViewSet):
    queryset = ItemPedido.objects.all()
    serializer_class = ItemPedidoSerializer
