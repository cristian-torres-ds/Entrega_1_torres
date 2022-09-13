from django.urls import path
from app_super.views import *
from app_super.views import ProductoList, ProductoDetalle, ProductoCreacion, ProductoUpdate, ProductoDelete


urlpatterns = [
    path('', inicio, name="inicio"),
    #-----PROVEEDORES
    path('add_proveedor/', proveedor_form, name="add_proveedor"), # los "name" son para colocar en los botones, en las html's
    path('busqueda_proveedor/', busqueda_proveedor, name="busqueda_proveedor"),
    path('buscar_proveedor/', buscar_proveedor, name="buscar_proveedor"),
    path('ver_proveedores/', ver_proveedores, name="ver_proveedores"),
    path('eliminar_proveedor/<id>', eliminar_proveedor, name="eliminar_proveedor"),
    path('editar_proveedor/<id>', editar_proveedor, name="editar_proveedor"),
    #-----EMPLEADOS
    path('add_empleado/', empleado_form, name="add_empleado"),
    path('busqueda_empleado/', busqueda_empleado, name="busqueda_empleado"),
    path('buscar_empleado/', buscar_empleado, name="buscar_empleado"),
    path('ver_empleados/', ver_empleados, name="ver_empleados"),
    path('eliminar_empleado/<id>', eliminar_empleado, name="eliminar_empleado"),
    path('editar_empleado/<id>', editar_empleado, name="editar_empleado"),
    #-----CLIENTES
    path('add_cliente/', cliente_form, name="add_cliente"),
    path('busqueda_cliente/', busqueda_cliente, name="busqueda_cliente"),
    path('buscar_cliente/', buscar_cliente, name="buscar_cliente"),
    path('ver_clientes/', ver_clientes, name="ver_clientes"),
    path('eliminar_cliente/<id>', eliminar_cliente, name="eliminar_cliente"),
    path('editar_cliente/<id>', editar_cliente, name="editar_cliente"),
    #-----PRODUCTOS
    path('producto/list/', ProductoList.as_view(), name='producto_list'),
    path('producto/<pk>', ProductoDetalle.as_view(), name='producto_detail'),
    path('producto/nuevo/', ProductoCreacion.as_view(), name='producto_new'),
    path('producto/editar/<pk>', ProductoUpdate.as_view(), name='producto_edit'),
    path('producto/eliminar/<pk>', ProductoDelete.as_view(), name='producto_delete'),

]