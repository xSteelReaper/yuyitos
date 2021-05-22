from django.shortcuts import render
from django.db import connection
import cx_Oracle

# Create your views here.


def productos(request):
    data={
        'productos': lista_productos(),
    }
    return render(request,'productos.html',data)

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
    return render(request, 'empleados.html',data)

def listado_empleados():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    
    cursor.callproc("SP_LISTAR_EMPLEADOS", [out_cur])
    
    lista = []
    for fila in out_cur:
        lista.append(fila)
        
    return lista
