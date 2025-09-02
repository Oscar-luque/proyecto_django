from django.urls import path
from . import views

app_name = 'fruteria'

urlpatterns = [
    path('frutas/', views.lista_frutas, name='lista_frutas'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('pedidos/<int:pedido_id>/', views.editar_pedido, name='editar_pedido'),
    path('pedidos/<int:pedido_id>/eliminar/', views.eliminar_pedido, name='eliminar_pedido'),
    path('frutas/crear/', views.crear_fruta, name='crear_fruta'),
    path('clientes/crear/', views.crear_cliente, name='crear_cliente'),
    path('pedidos/crear/', views.crear_pedido, name='crear_pedido'),
]