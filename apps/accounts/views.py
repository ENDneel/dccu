from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth.models import User
from django import forms

# Create your views here.
# Create your views here.
##SignUpForm formualrio por defecto de django para la creacion de usuario dentro del sistema
class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password check",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

#Metodo para iniciar sesion 
def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe el usuario
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                print("si entro el usuario ")
                return redirect('/gallery')

    # Si llegamos al final renderizamos el formulario
    return render(request, "gallery/login.html", {'form': form})

#metodo para cerrar sesion
def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')

#metodo para registrar a un usuario nuevo
def register_user(request):
    #mensajes para presentar los errores por pantalla
    msg     = None
    success = False
    #Si el metodo es Post realiza el registro
    if request.method == "POST":
        #validamos los datos de ingreso en el formulario 
        form = SignUpForm(request.POST)
        if form.is_valid():
            #guardamos el formulario o usuario
            form.save()
            #limpiamos los datos del formualrios
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg     = 'Usuario Creado- <a href="/login">Inicie Sesion</a>.'
            success = True
            
            #return redirect("/login/")

        else:
            msg = 'Ocurrio un error revise los campos'    
    else:
        form = SignUpForm()

    return render(request, "gallery/register.html", {"form": form, "msg" : msg, "success" : success })