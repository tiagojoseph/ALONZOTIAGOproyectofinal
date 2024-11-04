from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from usuarios.forms   import  FormularioDeCreacionDeUsuario
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from usuarios.forms import EditarPerfilForm




def login (request):

    formulario= AuthenticationForm()
 
    if request.method == "POST":
        formulario= AuthenticationForm (request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()

            django_login (request, usuario)

            return redirect ("inicio:inicio")



    return render (request, "usuarios/login.html", {"form": formulario} )


def registrarse (request):

    formulario = FormularioDeCreacionDeUsuario()
    if request.method == "POST":
        formulario = FormularioDeCreacionDeUsuario(request.POST)
        if formulario.is_valid():

            formulario.save()

            return redirect ("usuarios:login")

    return render (request, "usuarios/registrarse.html", {"form": formulario})



@login_required
def editar_perfil(request):
    usuario = request.user
    formulario = EditarPerfilForm(instance=usuario)

    if request.method == "POST":
        formulario = EditarPerfilForm(request.POST, instance=usuario)
        if formulario.is_valid():
            usuario = formulario.save(commit=False)  
            password = formulario.cleaned_data.get("password")

            if password: 
                usuario.set_password(password)

            usuario.save()  

            
            update_session_auth_hash(request, usuario) 

            return redirect("inicio:inicio") 

    return render(request, "usuarios/editar_perfil.html", {"form": formulario})
