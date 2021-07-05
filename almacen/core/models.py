from django.db import models
from datetime import date, datetime
# Create your models here.

class Empleado (models.Model):
    rut_empleado = models.CharField(max_length=11)
    nombre_empleado = models.CharField(max_length=100)
    direccion_empleado = models.CharField(max_length=200)
    telefono_empleado = models.CharField(max_length=20)
    cargo_empleado = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre_empleado

class Producto (models.Model):
    id_producto = models.AutoField(primary_key=True)
    familia_producto = models.CharField(max_length=50)
    fecha_vencimiento = models.DateField()
    tipo_producto = models.CharField(max_length=50, default='')
    descripcion = models.CharField(max_length=100, default='Descripcion')
    precio = models.IntegerField('Precio', default=1)
    nombre_producto = models.CharField(max_length=50, default='')
    marca_producto = models.CharField(max_length=50)
    stock = models.IntegerField('Stock', default=1)
    stock_critico = models.IntegerField('Critical stock', default=1)
    vigente = models.BooleanField(default=True)
    

    def __str__(self):
        return self.nombre_producto
    


class Cliente_Fiado (models.Model):
    rut_cliente = models.CharField(max_length=11)
    nombre_cliente = models.CharField(max_length=250)
    correo = models.CharField(max_length=75,default='correo@correo.com')
    direccion_cliente = models.CharField(max_length=200)
    telefono_cliente = models.CharField(max_length=20)
    estado_cliente = models.BooleanField('Enabled', default=True)

    def __str__(self):
        return self.nombre_cliente
    
class Tipo_Venta (models.Model):
    id_tipo= models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100, default='Descripcion')
    vigente=models.BooleanField(default=True)
    def __str__(self):
        return self.descripcion

    
class Venta (models.Model):
    id_venta=models.AutoField(primary_key=True)
    id_tipo = models.ForeignKey(Tipo_Venta, blank=True, null=True, on_delete=models.CASCADE)
    id_empleado=models.IntegerField()
    id_cliente =models.ForeignKey(Cliente_Fiado,blank=True, null=True, on_delete=models.CASCADE)
    monto = models.IntegerField(default=0)
    fecha_venta=models.DateTimeField(auto_now=True)
    descripcion=models.CharField(max_length=150)
    vigente=models.BooleanField(default=True)
    def int(self):
        return self.id_venta

class Venta_Detalle (models.Model):
    id_venta_detalle=models.AutoField(primary_key=True)
    id_venta=models.ForeignKey(Venta, on_delete=models.CASCADE)
    id_producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad=models.IntegerField()
    monto=models.BigIntegerField()
    vigente=models.BooleanField(default=True)
    def int(self):
        return self.id_venta_detalle

class Venta_Fiado (models.Model):
    id_venta_fiado = models.AutoField(primary_key=True)
    id_venta=models.ForeignKey(Venta, on_delete=models.CASCADE)
    id_cliente=models.ForeignKey(Cliente_Fiado, blank=True, null=True, on_delete=models.CASCADE)
    vigente=models.BooleanField(default=True)
    def __int__(self):
        return self.id_venta_fiado


class Reporte_Mensual (models.Model):
    id_reporte = models.AutoField(primary_key=True)
    total_productos = models.IntegerField()
    total_ganancias = models.IntegerField()
    venta_id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Proveedor (models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    rubro_empresa = models.CharField(max_length=100)
    nombre_empresa = models.CharField(max_length=100)
    nombre_proveedor = models.CharField(max_length=100)
    telefono_proveedor = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_empresa


class Orden_Pedido (models.Model):
    id_orden_pedido = models.AutoField(primary_key=True)
    cantidad_productos = models.IntegerField()
    precio_unitario = models.IntegerField()
    precio_total = models.IntegerField()
    descripcion = models.CharField(max_length=200, default = 'Descripcion')
    fecha_pedido = models.DateField()
    fecha_entrega = models.DateField()
    estado = models.BooleanField('Enabled', default=True)
    empleado_rut_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    proveedor_id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.descripcion

class Recepcion_Pedido (models.Model):
    id_recepcion_pedido = models.AutoField(primary_key=True)
    cantidad_productos = models.IntegerField()
    total_pedido = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    recepcion_id_orden_pedido = models.ForeignKey(
        Orden_Pedido, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion

class Tipo_Comprobante (models.Model):
    id_tipo_comprobante = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=200)
    def int(self):
        return self.id_tipo_comprobante
    
class Comprobante (models.Model):
    id_comprobante = models.AutoField(primary_key=True)
    id_tipo_comprobante=models.ForeignKey(Tipo_Comprobante, on_delete=models.CASCADE)
    id_venta=models.ForeignKey(Venta, on_delete=models.CASCADE)
    def int(self):
        return self.id_comprobante


