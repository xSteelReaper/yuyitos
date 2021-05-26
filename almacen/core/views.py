from django.shortcuts import render
from django.db import connection
import cx_Oracle
# Create your views here.


def productos(request):
    data={
        'productos': lista_productos(),
    }
    return render(request,'listar_productos.html',data)

def lista_productos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    
    cursor.callproc("SP_LISTAR_PRODUCTOS",[out_cur])
    
    lista = []
    for fila in out_cur:
        lista.append(fila)
    
    return lista   

"""aqui van los de agregar Productos"""

def agregarProducto(request):
    if request.method =='POST':
        familia_producto = request.POST.get('familia_producto')
        fecha_vencimiento = request.POST.get('fecha_vencimiento')
        tipo_producto = request.POST.get('tipo_producto')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        nombre_producto = request.POST.get('nombre_producto')
        marca_producto = request.POST.get('marca_producto')
        stock = request.POST.get('stock')
        stock_critico = request.POST.get('stock_critico')
        salida = add_producto(familia_producto, fecha_vencimiento,tipo_producto,descripcion,
        precio,nombre_producto,marca_producto,stock,stock_critico)
        """if salida == 1:              
            data['mensaje'] = 'agregado correctamente'         
        else:             
            data['mensaje'] = 'no se ha podido guardar'"""
            
    return render(request,'agregar_producto.html')

def add_producto(FAMILIA_PRODUCTO,FECHA_VENCIMIENTO,TIPO_PRODUCTO,DESCRIPCION,PRECIO,NOMBRE_PRODUCTO
,MARCA_PRODUCTO,STOCK,STOCK_CRITICO):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_PRODUCTO',[FAMILIA_PRODUCTO,FECHA_VENCIMIENTO,TIPO_PRODUCTO,DESCRIPCION,PRECIO,NOMBRE_PRODUCTO
,MARCA_PRODUCTO,STOCK,STOCK_CRITICO,salida]) 
    return salida.getvalue()   


"""def agregar_producto(familia_producto, fecha_vencimiento,tipo_producto,descripcion,
precio,nombre_producto,marca_producto,stock,stock_critico):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_PRODUCTO',[familia_producto, fecha_vencimiento,tipo_producto,descripcion,
precio,nombre_producto,marca_producto,stock,stock_critico,salida])
        
    return salida.getvalue() """



"""esto lo hizo el dani"""
def empleados (request):
    data = {
        'empleados':listado_empleados()
    }
    return render(request, 'listar_empleados.html',data)

def listado_empleados():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    
    cursor.callproc("SP_LISTAR_EMPLEADOS", [out_cur])
    
    lista = []
    for fila in out_cur:
        lista.append(fila)
        
    return lista


def agregarempleados (request):
    
    if request.method == 'POST':
        RUT_EMPLEADO = request.POST.get('rut_empleado')
        NOMBRE_EMPLEADO = request.POST.get('nombre_empleado')
        DIRECCION_EMPLEADO = request.POST.get('direccion_empleado')
        TELEFONO_EMPLEADO = request.POST.get('telefono_empleado')
        NOMBRE_USUARIO = request.POST.get('nombre_usuario')
        CONTRASEÑA_EMPLEADO = request.POST.get('contraseña_empleado')
        CARGO_EMPLEADO = request.POST.get('cargo_empleado')
        salida = agregar_empleado(RUT_EMPLEADO, NOMBRE_EMPLEADO, DIRECCION_EMPLEADO, TELEFONO_EMPLEADO,
                        NOMBRE_USUARIO, CONTRASEÑA_EMPLEADO, CARGO_EMPLEADO)
        
    
    return render(request, 'agregar_empleados.html')

def agregar_empleado(RUT_EMPLEADO, NOMBRE_EMPLEADO, DIRECCION_EMPLEADO, TELEFONO_EMPLEADO,
                        NOMBRE_USUARIO, CONTRASEÑA_EMPLEADO, CARGO_EMPLEADO):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_EMPLEADOS',[RUT_EMPLEADO, NOMBRE_EMPLEADO, DIRECCION_EMPLEADO, TELEFONO_EMPLEADO,
                        NOMBRE_USUARIO, CONTRASEÑA_EMPLEADO, CARGO_EMPLEADO, salida])
    return salida.getvalue()

#  LO HIZO SALOMOON
def proveedores (request):

    data = {
        'proveedores':listado_proveedores()
    }
    '''if salida == 1:
        data['mensaje'] = 'Agregado Correctamente'
        data['productos'] = listado_proveedores()
    else:
        data['mensaje'] = 'No se ha podido guardar' 
    '''
    #agregar_proveedor('chocolates','Costa','Pedro Martinez','+569 23848294')    
    return render(request, 'listar_proveedores.html',data)

def agregarproveedores(request):
    
    if request.method == 'POST':
        rubro_empresa = request.POST.get('Rubro Empresa')
        nombre_empresa = request.POST.get('Nombre Empresa')
        nombre_proveedor = request.POST.get('Nombre Proveedor')
        telefono_proveedor = request.POST.get('Telefono Proveedor')
        salida = agregar_proveedor(rubro_empresa,nombre_empresa,nombre_proveedor,telefono_proveedor)
        
    return render(request, 'agregar_proveedores.html')

def listado_proveedores():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    
    cursor.callproc("SP_LISTAR_PROVEEDORES", [out_cur])
    
    lista = [] 
    for fila in out_cur:
        lista.append(fila)
        
    return lista 

def agregar_proveedor(rubro_empresa,nombre_empresa,nombre_proveedor,telefono_proveedor):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_PROVEEDOR',[rubro_empresa,nombre_empresa,nombre_proveedor,telefono_proveedor,salida])
    return salida.getvalue()


# CRUD ORDEN DE PEDIDO
# Esto lo hizo Daniel

def ordenes(request):
    data = {
        'ordenes':listado_ordenes()
    }
    return render(request,'listar_ordenes.html',data)

def listado_ordenes():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    
    cursor.callproc("SP_LISTAR_ORDENES", [out_cur])
    
    lista = []
    for fila in out_cur:
        lista.append(fila)
        
    return lista


def agregar_ordenes (request):
    
    
    data={
        'empleados':listado_empleados(),
        'proveedores':listado_proveedores(),
    }
        
    if request.method == 'POST':
        CANTIDAD_PRODUCTOS = request.POST.get('cantidad_productos')
        PRECIO_UNITARIO = request.POST.get('precio_unitario')
        PRECIO_TOTAL = request.POST.get('precio_total')
        FECHA_PEDIDO = request.POST.get('fecha_pedido')
        FECHA_ENTREGA = request.POST.get('fecha_entrega')
        ESTADO = request.POST.get('estado')
        EMPLEADO_RUT_EMPLEADO_ID = request.POST.get('empleado')
        PROVEEDOR_ID_PROVEEDOR_ID = request.POST.get('proveedor')
        DESCRIPCION = request.POST.get('descripcion')
        salida = agregar_orden(CANTIDAD_PRODUCTOS, PRECIO_UNITARIO, PRECIO_TOTAL, FECHA_PEDIDO, 
                FECHA_ENTREGA, ESTADO, EMPLEADO_RUT_EMPLEADO_ID, PROVEEDOR_ID_PROVEEDOR_ID, DESCRIPCION)

        if salida == 1:
            data['mensaje'] = 'Agregado Correctamente'
            data['productos'] = listado_proveedores()
        else:
            data['mensaje'] = 'No se ha podido guardar'   
    
    return render(request, 'agregar_orden_pedido.html',data)

def agregar_orden(CANTIDAD_PRODUCTOS, PRECIO_UNITARIO, PRECIO_TOTAL, FECHA_PEDIDO, 
                FECHA_ENTREGA, ESTADO, EMPLEADO_RUT_EMPLEADO_ID, PROVEEDOR_ID_PROVEEDOR_ID, DESCRIPCION):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_ORDENES',[CANTIDAD_PRODUCTOS, PRECIO_UNITARIO, PRECIO_TOTAL, FECHA_PEDIDO, 
                FECHA_ENTREGA, ESTADO, EMPLEADO_RUT_EMPLEADO_ID, PROVEEDOR_ID_PROVEEDOR_ID, DESCRIPCION, salida])
    return salida.getvalue()