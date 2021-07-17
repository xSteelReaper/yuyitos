from django.urls import path
from .views import *

urlpatterns = [
    path('productos',productos, name ='productos'),
    path('agregarProducto',agregarProducto, name ='agregar_producto'),
    path('modificarProductos/<int:id>',modificarProducto, name ='editar_producto'),
    path('eliminarProducto/<int:idProducto>', eliminarProducto, name='eliminar_producto' ),      
    path('empleado', empleados, name = 'listar_empleados'),
    path('agregarEmpleado', agregarempleados, name= 'agregar_empleados'),
    path('modificarEmpleado/<int:id>', modificarEmpleado, name='modificar_empleado' ),
    path('eliminarEmpleado/<int:idEmpleado>', eliminarEmpleado, name='eliminar_empleado' ),
    path('listarProveedores', proveedores, name= 'listar_proveedores'),
    path('agregarProveedores', agregarproveedores, name = 'agregar_proveedores'),
    path('modificarProveedores/<int:id>', modificarProveedores, name='modificar_proveedores'),
    path('eliminarProveedores/<int:idProveedor>', eliminarProveedores, name='eliminar_proveedores'),
    path('registrar_cliente_fiado', registrarcliente, name='registrar_cliente' ),
    path('listarClienteFiado', cliente_fiado, name='cliente_fiado' ),
    path('modificarCliente/<int:id>', modificarCliente, name='modificar_cliente' ),
    path('eliminarCliente/<int:idCliente>', eliminarCliente, name='eliminar_cliente' ),
    path('listarorden', ordenes, name='listar_ordenes'),
    path('agregarOrden', agregar_ordenes, name='agregar_ordenes'),
    path('modificarPedido/<int:id>', modificarPedido, name='modificar_pedido' ),
    path('eliminarPedido/<int:idPedido>', eliminarPedido, name='eliminar_pedido' ),
    path('registro', pagina_registro, name='registro'),
    path('login', pagina_login, name='login'),
    path('', inicio, name='inicio'),
    path('logout', logout_user, name="logout"),
    path('listarRecepcion', recepcion, name='listar_recepcion_pedido'),
    path('modificarRecepcion/<int:id>', modificarRecepcion, name='modificar_recepcion' ),
    path('agregarRecepcion', agregarRecepcionPedido, name="agregarRecepcionPedido"),
    path('eliminarRecepcionPedido/<int:idRPedido>', eliminarRecepcionPedido, name='eliminar_recepcion' ),
]

