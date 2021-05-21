
from django.urls import path
from .views import *

urlpatterns = [
path('',productos, name ='productos'),
path('agregarProducto',agregarProductos, name ='agregar_producto'),       
path('empleado', empleados, name = 'empleados'),
]
