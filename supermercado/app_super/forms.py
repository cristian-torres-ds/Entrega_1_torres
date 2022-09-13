from django import forms

class ProveedorForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    telefono = forms.IntegerField()
    email = forms.EmailField()


class EmpleadoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    telefono = forms.IntegerField()
    email = forms.EmailField()
    nacimiento = forms.DateField()
    documento = forms.IntegerField()


class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    telefono = forms.IntegerField()
    email = forms.EmailField()


class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    marca = forms.CharField(max_length=50)
    cantidad = forms.IntegerField()