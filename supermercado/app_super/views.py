from django.shortcuts import render
from app_super.models import *
from app_super.forms import *
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def inicio(request):

    return render(request, "app_super/inicio.html")


#-------------PREVEEDORES-----------------------------------------------------------------------------------------


def proveedor_form(request):
    if request.method == 'POST':
        mi_formulario = ProveedorForm(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            # cleaned data devuelve un diccionario {'nombre':'abc', 'telefono':123, 'email':abc@xyz}
            proveedor = Proveedor(nombre = informacion['nombre'],
                                  telefono = informacion['telefono'],
                                  email = informacion['email'])
            proveedor.save()
            return render(request, "app_super/inicio.html", {"mensaje":"Proveedor creado exitosamente."})
    else:
        mi_formulario = ProveedorForm()
    return render(request, "app_super/add_proveedor.html", {"mi_formulario":mi_formulario})


def busqueda_proveedor(request):

    return render(request, "app_super/busqueda_proveedor.html")


def buscar_proveedor(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        nombres = Proveedor.objects.filter(nombre__icontains=nombre) # nombre=nombre
        return render(request, "app_super/buscar_proveedor.html", {"nombres":nombres})
    else:
        return render(request, "app_super/busqueda_proveedor.html", {"mensaje":"Ingrese un nombre."})


def ver_proveedores(request):
    lista_proveedores = Proveedor.objects.all()

    return render(request, "app_super/ver_proveedores.html", {"lista_proveedores" : lista_proveedores})


def eliminar_proveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)
    proveedor.delete()

    return ver_proveedores(request)


def editar_proveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)

    if request.method == 'POST':
        mi_formulario = ProveedorForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            proveedor.nombre = informacion['nombre']
            proveedor.telefono = informacion['telefono']
            proveedor.email = informacion['email']

            proveedor.save()

            return ver_proveedores(request)
    
    else:
        mi_formulario = ProveedorForm(initial={'nombre':proveedor.nombre,
                                                'telefono':proveedor.telefono,
                                                'email':proveedor.email})
    
    return render(request, "app_super/editar_proveedor.html", {'mi_formulario':mi_formulario, 'proveedor':proveedor})


#-------------EMPLEADOS-----------------------------------------------------------------------------------------


def empleado_form(request):
    if request.method == 'POST':
        mi_formulario = EmpleadoForm(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            empleado = Empleado(nombre = informacion['nombre'],
                                apellido = informacion['apellido'],
                                telefono = informacion['telefono'],
                                email = informacion['email'],
                                nacimiento = informacion['nacimiento'],
                                documento = informacion['documento'])
            empleado.save()
            return render(request, "app_super/inicio.html", {"mensaje":"Empleado creado exitosamente."})
    else:
        mi_formulario = EmpleadoForm()
    return render(request, "app_super/add_empleado.html", {"mi_formulario":mi_formulario})


def busqueda_empleado(request):

    return render(request, "app_super/busqueda_empleado.html")


def buscar_empleado(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        nombres = Empleado.objects.filter(nombre__icontains=nombre)
        return render(request, "app_super/buscar_empleado.html", {"nombres":nombres})
    else:
        return render(request, "app_super/busqueda_empleado.html", {"mensaje":"Ingrese un nombre."})


def ver_empleados(request):
    lista_empleados = Empleado.objects.all()

    return render(request, "app_super/ver_empleados.html", {"lista_empleados" : lista_empleados})


def eliminar_empleado(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()

    return ver_empleados(request)



def editar_empleado(request, id):
    empleado = Empleado.objects.get(id=id)

    if request.method == 'POST':
        mi_formulario = EmpleadoForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            empleado.nombre = informacion['nombre']
            empleado.apellido = informacion['apellido']
            empleado.telefono = informacion['telefono']
            empleado.email = informacion['email']
            empleado.nacimiento = informacion['nacimiento']
            empleado.documento = informacion['documento']

            empleado.save()

            return ver_empleados(request)
    
    else:
        mi_formulario = EmpleadoForm(initial={'nombre':empleado.nombre,
                                               'apellido':empleado.apellido,
                                               'telefono':empleado.telefono,
                                               'email':empleado.email,
                                               'nacimiento':empleado.nacimiento,
                                               'documento':empleado.documento,})
    
    return render(request, "app_super/editar_empleado.html", {'mi_formulario':mi_formulario, 'empleado':empleado})


#---------------CLIENTES--------------------------------------------------------------------------------


def cliente_form(request):
    if request.method == 'POST':
        mi_formulario = ClienteForm(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            cliente = Cliente(nombre = informacion['nombre'],
                              apellido = informacion['apellido'],
                              telefono = informacion['telefono'],
                              email = informacion['email'])
            cliente.save()
            return render(request, "app_super/inicio.html", {"mensaje":"Cliente creado exitosamente."})
    else:
        mi_formulario = ClienteForm()
    return render(request, "app_super/add_cliente.html", {"mi_formulario":mi_formulario})


def busqueda_cliente(request):

    return render(request, "app_super/busqueda_cliente.html")


def buscar_cliente(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        nombres = Cliente.objects.filter(nombre__icontains=nombre)
        return render(request, "app_super/buscar_cliente.html", {"nombres":nombres})
    else:
        return render(request, "app_super/busqueda_cliente.html", {"mensaje":"Ingrese un nombre."})


def ver_clientes(request):
    lista_clientes = Cliente.objects.all()

    return render(request, "app_super/ver_clientes.html", {"lista_clientes" : lista_clientes})


def eliminar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()

    return ver_clientes(request)


def editar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)

    if request.method == 'POST':
        mi_formulario = ClienteForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            cliente.nombre = informacion['nombre']
            cliente.apellido = informacion['apellido']
            cliente.telefono = informacion['telefono']
            cliente.email = informacion['email']

            cliente.save()

            return ver_clientes(request)
    
    else:
        mi_formulario = ClienteForm(initial={'nombre':cliente.nombre,
                                              'apellido':cliente.apellido,
                                              'telefono':cliente.telefono,
                                              'email':cliente.email})
    
    return render(request, "app_super/editar_cliente.html", {'mi_formulario':mi_formulario, 'cliente':cliente})


#---------------PRODUCTOS--------------------------------------------------------------------------------


class ProductoList(ListView):
    model = Producto
    template_name = "app_super/producto_list.html"

class ProductoDetalle(DetailView):
    model = Producto
    template_name = "app_super/producto_detalle.html"

class ProductoCreacion(CreateView):
    model = Producto
    success_url = reverse_lazy("producto_list")
    fields = ['nombre', 'marca', 'cantidad']

class ProductoUpdate(UpdateView):
    model = Producto
    success_url = reverse_lazy("producto_list")
    fields = ['nombre', 'marca', 'cantidad']

class ProductoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy("producto_list")