from django.urls import path
from .views import *

urlpatterns = [
    path('',productos, name ='productos'),
    path('agregarProducto',agregarProducto, name ='agregar_producto'),       
    path('empleado', empleados, name = 'listar_empleados'),
    path('agregarEmpleado', agregarempleados, name= 'agregar_empleados'),
    path('listarProveedores', proveedores, name= 'listar_proveedores'),
    
    path('listarorden', ordenes, name='listar_ordenes'),
    path('agregarOrden', agregar_ordenes, name='agregar_ordenes')
]

