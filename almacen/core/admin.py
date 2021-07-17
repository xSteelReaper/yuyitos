from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Producto)
admin.site.register(Empleado)
admin.site.register(Proveedor)
admin.site.register(Cliente_Fiado)
admin.site.register(Venta_Fiado)
admin.site.register(Venta)
admin.site.register(Orden_Pedido)
admin.site.register(Tipo_Comprobante)
admin.site.register(Comprobante)
admin.site.register(Venta_Detalle)
admin.site.register(Tipo_Venta)
admin.site.register(Recepcion_Pedido)




