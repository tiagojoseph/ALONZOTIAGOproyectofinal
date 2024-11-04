from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormularioDeCreacionDeUsuario(UserCreationForm):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField()
    password1 = forms.CharField(label= "contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label= "repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username","nombre","apellido", "email", "password1", "password2"]
        help_texts = {key: "" for key in fields}

class EditarPerfilForm(forms.ModelForm):
    password = forms.CharField(label="Nueva Contraseña", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label="Repetir Nueva Contraseña", widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password and password != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data