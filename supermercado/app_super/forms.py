from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']
        help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']
        # Quita los mensajes de ayuda.
        help_texts = {k:"" for k in fields}


class AvatarForm(forms.Form):
    imagen = forms.ImageField(label="imagen")