
from django.urls import path
from .views import *

urlpatterns = [
          path('',productos, name ='productos'),
]
