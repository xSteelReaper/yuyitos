from django.shortcuts import render
from django.db import connection
# Create your views here.


def productos(request):
    print(lista_productos())
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

