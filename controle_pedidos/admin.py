from django.contrib import admin

from .models import Cliente, Pedido, ItenPedido

admin.site.register(Cliente)

admin.site.register(Pedido)

admin.site.register(ItenPedido)



