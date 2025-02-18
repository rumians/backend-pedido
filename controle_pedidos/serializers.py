from rest_framework.serializers import ModelSerializer
from .models import Cliente, Pedido, ItemPedido

class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class PedidoSerializer(ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class ItemPedidoSerializer(ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = '__all__'
