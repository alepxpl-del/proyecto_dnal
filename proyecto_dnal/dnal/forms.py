from django import forms
from .models import Maquina, Reparacion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PerfilForm(forms.ModelForm):
    email = forms.EmailField(required=True, label="Correo Electrónico")
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
        
class MaquinaForm(forms.ModelForm):
    class Meta:
        model = Maquina
        fields = ("nombre", "tipo", "marca", "modelo", "descripcion")

class ReparacionForm(forms.ModelForm):
    class Meta:
        model = Reparacion
        fields = (
            "maquina",
            "problema",
            "trabajo_realizado",
            "repuestos",
            "costo_repuestos",
            "costo_mano_obra",
            "estado",
            "fecha_entrega",
        )

class MiFormularioDeCreacion(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(
        label='Contraseña', widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Confirmar contraseña', widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')
        help_texts = {key: '' for key in fields}