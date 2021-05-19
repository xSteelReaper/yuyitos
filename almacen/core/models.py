from django.db import models  
from datetime import date, datetime
# Create your models here.   


class Empleado (models.Model):
    rut_empleado = models.CharField(max_length=11)
    nombre_empleado = models.CharField(max_length=100)
    direccion_empleado = models.CharField(max_length=200)
    telefono_empleado = models.CharField(max_length=20)
    nombre_usuario = models.CharField(max_length=50)
    contraseña_empleado = models.CharField(max_length=50)
    cargo_empleado = models.BooleanField('Enabled', default=True)


class Venta (models.Model):
    id_venta = models.AutoField(primary_key=True)
    total_ventas = models.IntegerField()
    empleado_rut_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)

class Venta_Fiado (models.Model):
    id_venta_fiado = models.AutoField(primary_key=True)
    total_deudas_venta = models.IntegerField()
    venta_id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)


class Reporte_Mensual (models.Model):
    id_reporte = models.AutoField(primary_key=True)
    total_productos = models.IntegerField()
    total_ganancias = models.IntegerField()
    venta_id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    
    

class Proveedor (models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    rubro_empresa = models.CharField(max_length=100)
    nombre_empresa = models.CharField(max_length=100)
    nombre_proveedor = models.CharField(max_length=100)
    telefono_proveedor = models.CharField(max_length=20)


class Orden_Pedido (models.Model):
    id_orden_pedido = models.AutoField(primary_key=True)
    cantidad_productos = models.IntegerField()
    precio_unitario = models.IntegerField()
    precio_total = models.IntegerField()
    fecha_pedido = models.DateField()
    fecha_entrega = models.DateField()
    estado = models.BooleanField('Enabled', default=True)
    empleado_rut_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    proveedor_id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)



class Recepcion_Pedido (models.Model):
    id_recepcion_pedido = models.AutoField(primary_key=True)
    cantidad_productos = models.IntegerField()
    total_pedido = models.IntegerField()
    recepcion_id_orden_pedido = models.ForeignKey(Orden_Pedido, on_delete=models.CASCADE)

class Cliente_Fiado (models.Model):
    rut_cliente = models.CharField(max_length=11)
    nombre_cliente = models.CharField(max_length=100)
    direccion_cliente = models.CharField(max_length=200)
    telefono_cliente = models.CharField(max_length=20)
    estado_cliente = models.BooleanField('Enabled', default=True)
    monto_total_deuda = models.IntegerField()
    id_venta_fiado = models.ForeignKey(Venta_Fiado, on_delete=models.CASCADE)
    
class Comprobante_Fiado (models.Model):
    id_comprobate = models.AutoField(primary_key=True)
    fecha_venta = models.DateField()
    cantidad_productos = models.IntegerField()
    monto_neto = models.IntegerField()
    cliente_fiado_rut_cliente = models.ForeignKey(Cliente_Fiado, on_delete=models.CASCADE)


class Producto (models.Model):     
    id_producto = models.AutoField(primary_key=True)
    familia_producto = models.CharField(max_length=50)
    fecha_vencimiento = models.DateField()
    tipo_producto = models.CharField(max_length=50, default = '')
    descripcion = models.CharField(max_length=100, default = 'Descripcion')
    precio = models.IntegerField('Precio', default=1)
    nombre_producto = models.CharField(max_length=50, default = '')
    marca_producto = models.CharField(max_length=50)
    stock = models.IntegerField('Stock', default=1)
    stock_critico = models.IntegerField('Critical stock', default=1)
    
    def __str__(self):
        return self.nombre_producto


class Boleta (models.Model):
    id_boleta = models.AutoField(primary_key=True)
    fecha_venta = models.DateField()
    cantidad_productos = models.IntegerField()
    monto_neto = models.IntegerField()
    monto_total = models.IntegerField()
    venta_id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)