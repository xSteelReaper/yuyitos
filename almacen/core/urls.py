
from django.urls import path
from .views import *

urlpatterns = [
        path('',productos, name ='productos'),
        path('empleado', empleados, name = 'empleados'),
]
