from django.db import models

from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    data_pedido = models.DateField()
    valor_total = models.CharField(max_length=20)
    id_Cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.data_pedido} - {self.valor_total} - {self.id_Cliente.nome}"
    
class ItemPedido(models.Model):
    produto = models.CharField(max_length=100)
    quantidade = models.CharField(max_length=20)
    preco_unitario = models.CharField(max_length=20)
    id_Pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.produto} - {self.quantidade} - {self.preco_unitario}"