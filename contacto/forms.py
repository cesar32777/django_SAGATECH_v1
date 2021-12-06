from django import forms
from django.forms.fields import EmailField


class FormularioContacto(forms.Form):
    nombre=forms.CharField(label="Nombre", required=True, widget=forms.TextInput(attrs={'placeholder': 'Mi nombre'}))
    email=forms.EmailField(label="Email", required=True, widget=forms.TextInput(attrs={'placeholder': 'miEmail@email.com'}))
    asunto=forms.CharField(label="Asunto", required=True, widget=forms.TextInput(attrs={'placeholder': 'Servicio de mantenimiento a negocio'}))
    mensaje=forms.CharField(label="Mensaje", required=True, widget=forms.Textarea(attrs={'placeholder': 'Requiero mantenimiento de equipos para mi negocio...'}))