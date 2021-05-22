from django.shortcuts import render
from django.db import connection
import cx_Oracle
# Create your views here.


def productos(request):
    data={
        'productos': lista_productos()
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

"""aqui van los de agregar"""

def agregarProductos(request):
    data={
        'agregar_producto': agregar_productos()
    }
    return render(request,'agregar_producto.html',data)

def agregar_productos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    
    cursor.callproc("SP_AGREGAR_PRODUCTOS",[out_cur])
    
    lista = []
    for fila in out_cur:
        lista.append(fila)
    
    return lista  

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