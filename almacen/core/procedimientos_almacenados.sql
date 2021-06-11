---Procedimientos de Empleado---
create or replace procedure sp_agregar_empleados(
 v_RUT_EMPLEADO VARCHAR2,
 v_NOMBRE_EMPLEADO VARCHAR2,
 v_DIRECCION_EMPLEADO VARCHAR2,
 v_TELEFONO_EMPLEADO VARCHAR2,
 v_CARGO_EMPLEADO VARCHAR2,
 v_salida out number


)
IS

BEGIN
    insert into CORE_EMPLEADO (RUT_EMPLEADO, NOMBRE_EMPLEADO,
                DIRECCION_EMPLEADO, TELEFONO_EMPLEADO,
                CARGO_EMPLEADO)
    values (v_RUT_EMPLEADO, v_NOMBRE_EMPLEADO, v_DIRECCION_EMPLEADO,
            v_TELEFONO_EMPLEADO,
            v_CARGO_EMPLEADO);
    commit;
    v_salida:=1;


    exception

    when others then
        v_salida:=0;

END;


create or replace procedure sp_listar_empleados(empleados out SYS_REFCURSOR)
IS

BEGIN

    open empleados for SELECT * from core_empleado;

END;

create or replace PROCEDURE SP_ELIMINAR_EMPLEADO (idEmpleado number, v_salida out number)
IS
BEGIN
    DELETE FROM core_empleado where id = idEmpleado;
    commit;
    v_salida:=1;

    exception

    when others then
v_salida:=0;

END;


create or replace procedure SP_MODIFICAR_EMPLEADO(
id_modificando number, 
v_RUT_EMPLEADO VARCHAR2,
 v_NOMBRE_EMPLEADO VARCHAR2,
 v_DIRECCION_EMPLEADO VARCHAR2,
 v_TELEFONO_EMPLEADO VARCHAR2,
 v_CARGO_EMPLEADO VARCHAR2,
 v_salida out number
)is
begin
    UPDATE core_empleado set RUT_EMPLEADO = v_RUT_EMPLEADO,
    NOMBRE_EMPLEADO = v_NOMBRE_EMPLEADO,
    DIRECCION_EMPLEADO = v_DIRECCION_EMPLEADO, 
    TELEFONO_EMPLEADO = v_TELEFONO_EMPLEADO,
    CARGO_EMPLEADO = v_CARGO_EMPLEADO
    where id = id_modificando;
    commit;
    v_salida:=1;

exception

    when others then
v_salida:=0;

end;



create or replace procedure SP_TRAER_DATOS_EMPLEADO (idN number, datos out SYS_REFCURSOR )is
begin
    OPEN datos
    for
    SELECT * FROM core_empleado where id = idN;
end;



--------procedimientos orden de pedido-------------
create or replace procedure sp_listar_ordenes(ordenes out SYS_REFCURSOR)
IS

BEGIN

    open ordenes for SELECT * from core_orden_pedido;

END;



create or replace procedure sp_agregar_ordenes(
v_CANTIDAD_PRODUCTOS number,
v_PRECIO_UNITARIO number,
v_PRECIO_TOTAL number,
v_FECHA_PEDIDO date,
v_FECHA_ENTREGA date,
v_ESTADO number,
v_EMPLEADO_RUT_EMPLEADO_ID number,
v_PROVEEDOR_ID_PROVEEDOR_ID number,
v_DESCRIPCION NVARCHAR2,
v_salida out number


)
IS

BEGIN
    insert into CORE_ORDEN_PEDIDO (CANTIDAD_PRODUCTOS, PRECIO_UNITARIO, PRECIO_TOTAL, FECHA_PEDIDO, 
                FECHA_ENTREGA, ESTADO, EMPLEADO_RUT_EMPLEADO_ID, PROVEEDOR_ID_PROVEEDOR_ID, DESCRIPCION)
    values (v_CANTIDAD_PRODUCTOS, v_PRECIO_UNITARIO, v_PRECIO_TOTAL, v_FECHA_PEDIDO, v_FECHA_ENTREGA,
            v_ESTADO, v_EMPLEADO_RUT_EMPLEADO_ID, v_PROVEEDOR_ID_PROVEEDOR_ID, v_DESCRIPCION);



    commit;
    v_salida:=1;


    exception

    when others then
        v_salida:=0;

END;


create or replace PROCEDURE SP_ELIMINAR_PEDIDO (idPedido number, v_salida out number)
IS
BEGIN
    DELETE FROM CORE_ORDEN_PEDIDO where id_orden_pedido = idPedido;
    commit;
    v_salida:=1;

    exception

    when others then
v_salida:=0;

END;


create or replace procedure SP_MODIFICAR_PEDIDOS(
id_modificando number, 
v_CANTIDAD_PRODUCTOS number,
v_PRECIO_UNITARIO number,
v_PRECIO_TOTAL number,
v_FECHA_PEDIDO date,
v_FECHA_ENTREGA date,
v_ESTADO number,
v_DESCRIPCION NVARCHAR2,
v_salida out number
)is
begin
    UPDATE CORE_ORDEN_PEDIDO set CANTIDAD_PRODUCTOS = v_CANTIDAD_PRODUCTOS,
    PRECIO_UNITARIO = v_PRECIO_UNITARIO,
    PRECIO_TOTAL = v_PRECIO_TOTAL, 
    FECHA_PEDIDO = v_FECHA_PEDIDO,
    FECHA_ENTREGA = v_FECHA_ENTREGA,
    ESTADO = v_ESTADO,
    DESCRIPCION = v_DESCRIPCION  

    where ID_ORDEN_PEDIDO = id_modificando;
    commit;
    v_salida:=1;

exception

    when others then
v_salida:=0;

end;



create or replace procedure SP_TRAER_DATOS_PEDIDO (idN number, datos out SYS_REFCURSOR )is
begin
    OPEN datos
    for
    SELECT * FROM CORE_ORDEN_PEDIDO where ID_ORDEN_PEDIDO = idN;
end;


---Procedimientos proveedores---
create or replace procedure sp_listar_proveedores(proveedores out SYS_REFCURSOR)
IS

BEGIN

    OPEN proveedores for select * from core_proveedor;
END;

create or replace procedure sp_agregar_proveedor(
    v_rubroEmpresa varchar2,
    v_nombreEmpresa varchar2,
    v_nombreProveedor varchar2,
    v_telefonoProveedor varchar2,
    v_salida out number
)
IS
BEGIN
    insert into core_proveedor(rubro_empresa,nombre_empresa,nombre_proveedor,telefono_proveedor)
    values(v_rubroEmpresa, v_nombreEmpresa, v_nombreProveedor, v_telefonoProveedor);
    COMMIT;
    v_salida:=1;

    exception

    when others then
        v_salida:= 0; 
END;

create or replace procedure SP_MODIFICAR_PROVEEDORES(
    id_modificando number, 
    v_rubroEmpresa varchar2,
    v_nombreEmpresa varchar2,
    v_nombreProveedor varchar2, 
    v_telefonoProveedor varchar2, 
    v_salida out number)
is
begin
    UPDATE CORE_PROVEEDOR 
        SET rubro_empresa = v_rubroEmpresa,
            nombre_empresa = v_nombreEmpresa,
            nombre_proveedor = v_nombreProveedor, 
            telefono_proveedor = v_telefonoProveedor
    where ID_PROVEEDOR = id_modificando;
    commit;
    v_salida:=1;

exception

    when others then
v_salida:=0;

end;

create or replace procedure SP_TRAER_DATOS_PROVEEDORES (idN number, datos out SYS_REFCURSOR )is
begin
    OPEN datos
    for
    SELECT * FROM core_proveedor where ID_PROVEEDOR = idN;
end;

create or replace procedure SP_ELIMINAR_PROVEEDORES (idProveedor NUMBER, v_salida out number
)
IS
begin
    DELETE FROM core_proveedor where ID_PROVEEDOR = idProveedor;
    commit;
    v_salida:=1;

exception

    when others then
v_salida:=0;
end;


---Procedimientos producto---

create or replace procedure sp_agregar_producto(v_familia_producto varchar2,v_fecha_vencimiento DATE,
v_tipo_producto varchar2,v_descripcion	varchar2,v_precio NUMBER,v_nombre_producto varchar2,v_marca_producto varchar2,
v_stock NUMBER,v_stock_critico NUMBER,v_salida out number
)is 
begin
    insert into core_producto(familia_producto, fecha_vencimiento,tipo_producto,descripcion,
    precio,nombre_producto,marca_producto,stock,stock_critico)
    values(v_familia_producto, v_fecha_vencimiento,v_tipo_producto,v_descripcion,v_precio,v_nombre_producto,v_marca_producto,v_stock,v_stock_critico);
    commit; 
    v_salida:=1;

    exception

    when others then
    v_salida:=0;

end;

create or replace PROCEDURE SP_ELIMINAR_PRODUCTO (idProducto number, v_salida out number)
IS
BEGIN
    DELETE FROM core_producto where id_producto = idProducto;
    commit;
    v_salida:=1;

    exception

    when others then
v_salida:=0;

END;

create or replace procedure sp_listar_productos (productos out SYS_REFCURSOR)
is
begin
     open productos for select * from core_producto;
end;

create or replace procedure sp_modificar_producto
(id_modificando number,
v_familia_producto varchar2,
v_fecha_vencimiento DATE,
v_tipo_producto varchar2,
v_descripcion	varchar2,
v_precio NUMBER,
v_nombre_producto varchar2,
v_marca_producto varchar2,
v_stock NUMBER,
v_stock_critico NUMBER,v_salida out number
)is
begin
    UPDATE core_producto set FAMILIA_PRODUCTO = v_familia_producto,
FECHA_VENCIMIENTO=v_fecha_vencimiento,
TIPO_PRODUCTO=v_tipo_producto,
DESCRIPCION=v_descripcion,
PRECIO=v_precio,
NOMBRE_PRODUCTO=v_nombre_producto,
MARCA_PRODUCTO=v_marca_producto,
STOCK=v_stock,
STOCK_CRITICO=v_stock_critico
    where id_producto = id_modificando;
    commit;
    v_salida:=1;

exception

    when others then
v_salida:=0;
end;

create or replace procedure SP_TRAER_DATOS_PRODUCTO (idN number, datos out SYS_REFCURSOR )is
begin
    OPEN datos
    for
    SELECT * FROM core_producto where id_producto = idN;
end;


---Procedimientos Cliente Fiado---

create or replace procedure SP_ELIMINAR_CLIENTE_FIADO (idCliente NUMBER, v_salida out number
)is
begin
    DELETE FROM core_cliente_fiado where id = idCliente;
    commit;
    v_salida:=1;

exception

    when others then
v_salida:=0;

end;

create or replace procedure sp_listar_cliente (cliente_fiado out SYS_REFCURSOR)
is
begin
    open cliente_fiado
    for
    select *
    from core_cliente_fiado;
end;

create or replace PROCEDURE SP_LISTAR_VENTAS_BY_EMPLEADO (ventas_empleados out SYS_REFCURSOR) IS
BEGIN
  OPEN ventas_empleados FOR SELECT * FROM core_venta p JOIN core_empleado e ON e.id = p.empleado_rut_empleado_id;
END;

create or replace procedure SP_MODIFICAR_CLIENTE_FIADO
(id_modificando number, v_rut_cliente varchar2,v_nombre_cliente varchar2, v_correo varchar2,
v_direccion_cliente varchar2,v_telefono_cliente varchar2,v_monto_total_deuda NUMBER, v_salida out number
)is
begin
    UPDATE core_cliente_fiado set rut_cliente = v_rut_cliente,
     nombre_cliente = v_nombre_cliente,
     correo = v_correo,
     direccion_cliente = v_direccion_cliente, 
     telefono_cliente = v_telefono_cliente
    where id = id_modificando;
    commit;
    v_salida:=1;

exception

    when others then
v_salida:=0;

end;

create or replace procedure sp_registrar_cliente_fiado (v_rut_cliente varchar2,v_nombre_cliente varchar2, v_correo varchar2,
v_direccion_cliente varchar2,v_telefono_cliente varchar2,v_estado_cliente NUMBER, v_salida out number
)is
begin
    insert into core_cliente_fiado
        (rut_cliente, nombre_cliente,correo, direccion_cliente,telefono_cliente,
        estado_cliente)
    values(v_rut_cliente, v_nombre_cliente, v_correo, v_direccion_cliente, v_telefono_cliente, v_estado_cliente);
    commit;
    v_salida:=1;

exception

    when others then
v_salida:=0;

end;

create or replace procedure SP_TRAER_DATOS_CLIENTE (idN number, datos out SYS_REFCURSOR )is
begin
    OPEN datos
    for
    SELECT * FROM core_cliente_fiado where id = idN;
end;