
create or replace procedure sp_listar_productos (productos out SYS_REFCURSOR)
is
begin
     open productos for select * from core_producto;
end;


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


