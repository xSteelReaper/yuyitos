
create or replace procedure sp_listar_productos (productos out SYS_REFCURSOR)
is
begin
     open productos for select * from core_producto;
end;


