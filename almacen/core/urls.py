from django.urls import path
from .views import *

urlpatterns = [
    path('',productos, name ='productos'),
    path('agregarProducto',agregarProducto, name ='agregar_producto'),       
    path('empleado', empleados, name = 'listar_empleados'),
    path('agregarEmpleado', agregarempleados, name= 'agregar_empleados'),
    path('listarProveedores', proveedores, name= 'listar_proveedores')
]
