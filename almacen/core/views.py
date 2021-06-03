from django.http import request
from django.shortcuts import redirect, render
from django.db import connection
import cx_Oracle
from django.contrib import messages
# ------------ login y registro ----------
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
# ------- bloquear paginas ------
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="login")
def productos(request):
    data = {
        'productos': lista_productos(),
    }
    return render(request, 'listar_productos.html', data)


def lista_productos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_PRODUCTOS", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


"""aqui van los de agregar Productos"""

@login_required(login_url="login")
def agregarProducto(request):
    if request.method == 'POST':
        familia_producto = request.POST.get('familia_producto')
        fecha_vencimiento = request.POST.get('fecha_vencimiento')
        tipo_producto = request.POST.get('tipo_producto')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        nombre_producto = request.POST.get('nombre_producto')
        marca_producto = request.POST.get('marca_producto')
        stock = request.POST.get('stock')
        stock_critico = request.POST.get('stock_critico')
        salida = add_producto(familia_producto, fecha_vencimiento, tipo_producto, descripcion,
                              precio, nombre_producto, marca_producto, stock, stock_critico)
        if salida == 1:
            # data['mensaje'] = 'Agregado Correctamente'
            messages.success(request, "Agregado correctamente")
            
        else:
            # data['mensaje'] = 'No se ha podido guardar'
            messages.success(request, "No se pudo agregar")

    return render(request, 'agregar_producto.html')


def add_producto(FAMILIA_PRODUCTO, FECHA_VENCIMIENTO, TIPO_PRODUCTO, DESCRIPCION, PRECIO, NOMBRE_PRODUCTO, MARCA_PRODUCTO, STOCK, STOCK_CRITICO):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_PRODUCTO', [FAMILIA_PRODUCTO, FECHA_VENCIMIENTO, TIPO_PRODUCTO,
                    DESCRIPCION, PRECIO, NOMBRE_PRODUCTO, MARCA_PRODUCTO, STOCK, STOCK_CRITICO, salida])
    return salida.getvalue()

@login_required(login_url="login")
def modificarProducto(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_TRAER_DATOS_PRODUCTO", [id, out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    id = lista[0][0]
    familia = lista[0][1]
    vencimiento = lista[0][2]
    tipo = lista[0][3]
    descripcion = lista[0][4]
    precio = lista[0][5]
    nombre = lista[0][6]
    marca = lista[0][7]
    stock = lista[0][8]
    critico = lista[0][9]
    
    
    if request.method == 'POST':
        id_modificando = request.POST.get('id_editando')
        FAMILIA_PRODUCTO = request.POST.get('familia_producto_edit')
        FECHA_VENCIMIENTO = request.POST.get('fecha_vencimiento_edit')
        TIPO_PRODUCTO = request.POST.get('tipo_producto_edit')
        DESCRIPCION = request.POST.get('descripcion_edit')
        PRECIO = request.POST.get('precio_edit')
        NOMBRE_PRODUCTO = request.POST.get('nombre_producto_edit')
        MARCA_PRODUCTO = request.POST.get('marca_producto_edit')
        STOCK = request.POST.get('stock_edit')
        STOCK_CRITICO = request.POST.get('stock_critico_edit')
        salida = modificar_producto(id_modificando,FAMILIA_PRODUCTO, FECHA_VENCIMIENTO, TIPO_PRODUCTO, DESCRIPCION,
                              PRECIO, NOMBRE_PRODUCTO, MARCA_PRODUCTO, STOCK, STOCK_CRITICO)
        messages.success(request, "modificado correctamente")

    return render(request, 'editar_producto.html', {
        "Listado": lista,
        "id": id,
        "familia" : familia,
        "vencimiento": vencimiento,
        "tipo": tipo,
        "descripcion": descripcion,
        "precio": precio,
        "nombre": nombre,
        "marca": marca,
        "stock": stock,
        "critico": critico,
    })


def modificar_producto(id_modificando,FAMILIA_PRODUCTO, FECHA_VENCIMIENTO, TIPO_PRODUCTO, DESCRIPCION,
                              PRECIO, NOMBRE_PRODUCTO, MARCA_PRODUCTO, STOCK, STOCK_CRITICO):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_MODIFICAR_PRODUCTO', [
                    id_modificando,FAMILIA_PRODUCTO, FECHA_VENCIMIENTO, TIPO_PRODUCTO, DESCRIPCION,
                              PRECIO, NOMBRE_PRODUCTO, MARCA_PRODUCTO, STOCK, STOCK_CRITICO, salida])
    return salida.getvalue()

@login_required(login_url="login")
def eliminarProducto(request, idProducto):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_ELIMINAR_PRODUCTO', [idProducto,  salida])
    data = {
        'productos': lista_productos(),
    }
    
    messages.success(request, "eliminado correctamente")
    
    return render(request, 'listar_productos.html', data)



# --------- CRUD EMPLEDOS ------------

@login_required(login_url="login")
def empleados(request):
    data = {
        'empleados': listado_empleados()
    }
    return render(request, 'listar_empleados.html', data)


def listado_empleados():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_EMPLEADOS", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista

@login_required(login_url="login")
def agregarempleados(request):

    if request.method == 'POST':
        RUT_EMPLEADO = request.POST.get('rut_empleado')
        NOMBRE_EMPLEADO = request.POST.get('nombre_empleado')
        DIRECCION_EMPLEADO = request.POST.get('direccion_empleado')
        TELEFONO_EMPLEADO = request.POST.get('telefono_empleado')
        CARGO_EMPLEADO = request.POST.get('cargo_empleado')
        salida = agregar_empleado(RUT_EMPLEADO, NOMBRE_EMPLEADO, DIRECCION_EMPLEADO, TELEFONO_EMPLEADO,
                                  CARGO_EMPLEADO)
        
        if salida == 1:
            # data['mensaje'] = 'Agregado Correctamente'
            messages.success(request, "Agregado correctamente")
            
        else:
            # data['mensaje'] = 'No se ha podido guardar'
            messages.success(request, "No se pudo agregar")

    return render(request, 'agregar_empleados.html')


def agregar_empleado(RUT_EMPLEADO, NOMBRE_EMPLEADO, DIRECCION_EMPLEADO, TELEFONO_EMPLEADO,
                      CARGO_EMPLEADO):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_EMPLEADOS', [RUT_EMPLEADO, NOMBRE_EMPLEADO, DIRECCION_EMPLEADO, TELEFONO_EMPLEADO,
                                             CARGO_EMPLEADO, salida])
    return salida.getvalue()

@login_required(login_url="login")
def modificarEmpleado(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_TRAER_DATOS_EMPLEADO", [id, out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    
    id = lista[0][0]
    rut = lista[0][1]
    nombre = lista[0][2]
    direccion = lista[0][3]
    telefono = lista[0][4]
    cargo = lista[0][5]
    
    if request.method == 'POST':
        id_modificando = request.POST.get('id_editando')
        RUT_EMPLEADO = request.POST.get('rut_empleado_edit')
        NOMBRE_EMPLEADO = request.POST.get('nombre_empleado_edit')
        DIRECCION_EMPLEADO = request.POST.get('direccion_empleado_edit')
        TELEFONO_EMPLEADO = request.POST.get('telefono_empleado_edit')
        CARGO_EMPLEADO = request.POST.get('cargo_empleado_edit')
        salida = modificar_empleado(id_modificando, RUT_EMPLEADO, NOMBRE_EMPLEADO, DIRECCION_EMPLEADO, TELEFONO_EMPLEADO,
                                  CARGO_EMPLEADO)
        messages.success(request, "modificado correctamente")
        
    return render(request, 'editar_empleados.html', {
        "Listado" : lista,
        "id" : id,
        "rut" : rut,
        "nombre" : nombre,
        "direccion" : direccion,
        "telefono" : telefono,
        "cargo" : cargo,
    })
    
def modificar_empleado(id_modificando, RUT_EMPLEADO, NOMBRE_EMPLEADO, DIRECCION_EMPLEADO, TELEFONO_EMPLEADO,
                                  CARGO_EMPLEADO):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_MODIFICAR_EMPLEADO', [
                    id_modificando, RUT_EMPLEADO, NOMBRE_EMPLEADO, DIRECCION_EMPLEADO, TELEFONO_EMPLEADO,
                                  CARGO_EMPLEADO, salida])
    return salida.getvalue()




@login_required(login_url="login")
def eliminarEmpleado(request, idEmpleado):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_ELIMINAR_EMPLEADO', [idEmpleado,  salida])
    data = {
        'empleados': listado_empleados(),
    }
    
    messages.success(request, "eliminado correctamente")
    
    return render(request, 'listar_empleados.html', data)


#  CRUD PROVEEDORES
@login_required(login_url="login")
def proveedores(request):
    data = {
        'proveedores': listado_proveedores()
    }
    '''if salida == 1:
        data['mensaje'] = 'Agregado Correctamente'
        data['productos'] = listado_proveedores()
    else:
        data['mensaje'] = 'No se ha podido guardar'     '''
    return render(request, 'listar_proveedores.html', data)

@login_required(login_url="login")
def agregarproveedores(request):
    if request.method == 'POST':
        rubro_empresa = request.POST.get('Rubro Empresa')
        nombre_empresa = request.POST.get('Nombre Empresa')
        nombre_proveedor = request.POST.get('Nombre Proveedor')
        telefono_proveedor = request.POST.get('Telefono Proveedor')
        salida = agregar_proveedor(
            rubro_empresa, nombre_empresa, nombre_proveedor, telefono_proveedor)
        # if salida == 1:
        #     data['mensaje'] = 'Agregado Correctamente'
        #     data['productos'] = listado_proveedores()
        # else:
        #     data['mensaje'] = 'No se ha podido guardar'

    # return render(request, 'listar_proveedores.html', data)

    # salida = agregar_proveedor(
    #     rubro_empresa, nombre_empresa, nombre_proveedor, telefono_proveedor)
        if salida == 1:
            # data['mensaje'] = 'Agregado Correctamente'
            messages.success(request, "Agregado correctamente")
            
        else:
            # data['mensaje'] = 'No se ha podido guardar'
            messages.success(request, "No se pudo agregar")

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

def agregar_proveedor(rubro_empresa, nombre_empresa, nombre_proveedor, telefono_proveedor):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_PROVEEDOR', [
                    rubro_empresa, nombre_empresa, nombre_proveedor, telefono_proveedor, salida])
    return salida.getvalue()

@login_required(login_url="login")
def modificarProveedores(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_TRAER_DATOS_PROVEEDORES", [id, out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    
    id = lista[0][0]
    rubroEmpresa = lista[0][1]
    nombreEmpresa = lista[0][2]
    nombreProveedor = lista[0][3]
    telefonoProveedor = lista[0][4]
    
    if request.method == 'POST':
        id_modificando = request.POST.get('id_editando')
        RUBRO_EMPRESA = request.POST.get('rubro_empresa_edit')
        NOMBRE_EMPRESA = request.POST.get('nombre_empresa_edit')
        NOMBRE_PROVEEDOR = request.POST.get('nombre_proveedor_edit')
        TELEFONO_PROVEEDOR = request.POST.get('telefono_proveedor_edit')
        salida = modificar_proveedor(id_modificando, RUBRO_EMPRESA, NOMBRE_EMPRESA, NOMBRE_PROVEEDOR, TELEFONO_PROVEEDOR)
        messages.success(request, "modificado correctamente")
        
    return render(request, 'editar_proveedores.html', {
        "Listado" : lista,
        "id" : id,
        "rubroEmpresa" : rubroEmpresa,
        "nombreEmpresa" : nombreEmpresa,
        "nombreProveedor" : nombreProveedor,
        "telefonoProveedor" : telefonoProveedor
    })
    
def modificar_proveedor(id_modificando, RUBRO_EMPRESA, NOMBRE_EMPRESA, NOMBRE_PROVEEDOR, TELEFONO_PROVEEDOR):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_MODIFICAR_PROVEEDORES', [
                    id_modificando, RUBRO_EMPRESA, NOMBRE_EMPRESA, NOMBRE_PROVEEDOR, TELEFONO_PROVEEDOR, salida])
    return salida.getvalue()

@login_required(login_url="login")
def eliminarProveedores(request, idProveedor):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_ELIMINAR_PROVEEDORES', [idProveedor,  salida])
    data = {
        'proveedores': listado_proveedores(),
    }
    
    messages.success(request, "eliminado correctamente")
    
    return render(request, 'listar_proveedores.html', data)

# ----------------------------  felipe listar
@login_required(login_url="login")
def cliente_fiado(request):
    data = {
        'cliente_fiado': listar_cliente_fiado(),

    }

    return render(request, 'listar_cliente_fiado.html', data)


def listar_cliente_fiado():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_CLIENTE", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


# ------------- Agregar cliente fiado ------------
@login_required(login_url="login")
def registrarcliente(request):
    data = {
        'ventas': traeVentasByEmpleado(),    
    }
    if request.method == 'POST':
        rut_cliente = request.POST.get('rut_cliente')
        nombre_cliente = request.POST.get('nombre_cliente')
        direccion_cliente = request.POST.get('direccion_cliente')
        telefono_cliente = request.POST.get('telefono_cliente')
        estado_cliente = 1
        monto_total_deuda = request.POST.get('monto_total_deuda')
        id_venta = request.POST.get('venta_id')
        salida = registrar_fiado(rut_cliente, nombre_cliente, direccion_cliente, telefono_cliente,
                                 estado_cliente, monto_total_deuda, id_venta)
        
        
        if salida == 1:
            # data['mensaje'] = 'Agregado Correctamente'
            messages.success(request, "Agregado correctamente")
            
        else:
            # data['mensaje'] = 'No se ha podido guardar'
            messages.success(request, "No se pudo agregar")

    return render(request, 'registrar_cliente_fiado.html', data)


def registrar_fiado(rut_cliente, nombre_cliente, direccion_cliente, telefono_cliente, estado_cliente, monto_total_deuda, id_venta):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_REGISTRAR_CLIENTE_FIADO', [
                    rut_cliente, nombre_cliente, direccion_cliente, telefono_cliente, estado_cliente, monto_total_deuda, id_venta, salida])
    return salida.getvalue()

# ----- seleccionar ventas disponibles para fiados


def traeVentasByEmpleado():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_VENTAS_BY_EMPLEADO", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


# ------------------ Editar cliente fiado ------------------
@login_required(login_url="login")
def modificarCliente(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_TRAER_DATOS_CLIENTE", [id, out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    id = lista[0][0]
    rut = lista[0][1]
    nombre = lista[0][2]
    direccion = lista[0][3]
    telefono = lista[0][4]
    monto = lista[0][6]

    if request.method == 'POST':
        id_modificando = request.POST.get('id_editando')
        rut_cliente = request.POST.get('rut_cliente_mod')
        nombre_cliente = request.POST.get('nombre_cliente_mod')
        direccion_cliente = request.POST.get('direccion_cliente_mod')
        telefono_cliente = request.POST.get('telefono_cliente_mod')
        monto_total_deuda = request.POST.get('monto_total_deuda_mod')
        salida = modificar_fiado(id_modificando, rut_cliente, nombre_cliente,
                                 direccion_cliente, telefono_cliente, monto_total_deuda)
        messages.success(request, "modificado correctamente") 
     

    return render(request, 'editar_cliente_fiado.html', {
        "Listado": lista,
        "id": id,
        "rut": rut,
        "nombre": nombre,
        "direccion": direccion,
        "telefono": telefono,
        "monto": monto,
    })


def modificar_fiado(id_modificando, rut_cliente, nombre_cliente, direccion_cliente, telefono_cliente, monto_total_deuda):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_MODIFICAR_CLIENTE_FIADO', [
                    id_modificando, rut_cliente, nombre_cliente, direccion_cliente, telefono_cliente, monto_total_deuda, salida])
    
    return salida.getvalue()

@login_required(login_url="login")
def eliminarCliente(request, idCliente):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_ELIMINAR_CLIENTE_FIADO', [idCliente,  salida])
    data = {
        'cliente_fiado': listar_cliente_fiado(),
    }
    
    messages.success(request, "eliminado correctamente")

    return render(request, 'listar_cliente_fiado.html', data)


# CRUD ORDEN DE PEDIDO
# Esto lo hizo Daniel
@login_required(login_url="login")
def ordenes(request):
    data = {
        'ordenes': listado_ordenes()
    }
    return render(request, 'listar_ordenes.html', data)


def listado_ordenes():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_ORDENES", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista

@login_required(login_url="login")
def agregar_ordenes(request):

    data = {
        'empleados': listado_empleados(),
        'proveedores': listado_proveedores(),
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
            # data['mensaje'] = 'Agregado Correctamente'
            messages.success(request, "Agregado correctamente")
            
        else:
            # data['mensaje'] = 'No se ha podido guardar'
            messages.success(request, "No se pudo agregar")

    return render(request, 'agregar_orden_pedido.html', data)


def agregar_orden(CANTIDAD_PRODUCTOS, PRECIO_UNITARIO, PRECIO_TOTAL, FECHA_PEDIDO,
                  FECHA_ENTREGA, ESTADO, EMPLEADO_RUT_EMPLEADO_ID, PROVEEDOR_ID_PROVEEDOR_ID, DESCRIPCION):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_ORDENES', [CANTIDAD_PRODUCTOS, PRECIO_UNITARIO, PRECIO_TOTAL, FECHA_PEDIDO,
                                           FECHA_ENTREGA, ESTADO, EMPLEADO_RUT_EMPLEADO_ID, PROVEEDOR_ID_PROVEEDOR_ID, DESCRIPCION, salida])
    return salida.getvalue()


@login_required(login_url="login")
def modificarPedido(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_TRAER_DATOS_PEDIDO", [id, out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    
    id = lista[0][0]
    cantidad = lista[0][1]
    precio_unitario = lista[0][2]
    precio_total = lista[0][3]
    fecha_pedido = lista[0][4]
    fecha_entrega = lista[0][5]
    estado = lista[0][6]
    descripcion = lista[0][9]
    
    if request.method == 'POST':
        id_modificando = request.POST.get('id_editando')
        CANTIDAD_PRODUCTOS = request.POST.get('cantidad_productos_edit')
        PRECIO_UNITARIO = request.POST.get('precio_unitario_edit')
        PRECIO_TOTAL = request.POST.get('precio_total_edit')
        FECHA_PEDIDO = request.POST.get('fecha_pedido_edit')
        FECHA_ENTREGA = request.POST.get('fecha_entrega_edit')
        ESTADO = request.POST.get('estado_edit')
        DESCRIPCION = request.POST.get('descripcion_edit')
        salida = modificar_pedido(id_modificando, CANTIDAD_PRODUCTOS, PRECIO_UNITARIO, PRECIO_TOTAL, FECHA_PEDIDO,
                               FECHA_ENTREGA, ESTADO, DESCRIPCION)
        messages.success(request, "modificado correctamente")
        
    return render(request, 'editar_pedidos.html', {
        "Listado" : lista,
        "id" : id,
        "cantidad" : cantidad,
        "precio_unitario" : precio_unitario,
        "precio_total" : precio_total,
        "fecha_pedido" : fecha_pedido,
        "fecha_entrega" : fecha_entrega,
        "estado" : estado,
        "descripcion" : descripcion,
    })
    
def modificar_pedido(id_modificando, CANTIDAD_PRODUCTOS, PRECIO_UNITARIO, PRECIO_TOTAL, FECHA_PEDIDO,
                               FECHA_ENTREGA, ESTADO, DESCRIPCION):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_MODIFICAR_PEDIDOS', [
                    id_modificando, CANTIDAD_PRODUCTOS, PRECIO_UNITARIO, PRECIO_TOTAL, FECHA_PEDIDO,
                               FECHA_ENTREGA, ESTADO, DESCRIPCION, salida])
    return salida.getvalue()

@login_required(login_url="login")
def eliminarPedido(request, idPedido):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_ELIMINAR_PEDIDO', [idPedido,  salida])
    data = {
        'ordenes': listado_ordenes()
    }
    messages.success(request, "eliminado correctamente")
    return render(request, 'listar_ordenes.html', data)

# ------------------ registro login ---------------

def pagina_registro(request):
    
    register_form =RegisterForm()
    
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Te has registrado correctamente')
            
            return redirect('registrar_cliente')
    
    return render(request, 'registro.html', {
        'register_form': register_form
    })
        
def pagina_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            messages.warning(request, 'No estas registrado')
    
    return render(request, 'login.html')

def inicio(request):
    
    return render (request, 'inicio.html')

def logout_user(request):
    logout(request)
    return redirect('login')