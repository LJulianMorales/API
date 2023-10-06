from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from api.forms import LoginForm 

#Django plantilla
from django.shortcuts import render, redirect
from api.forms import LoginForm, RegistrationForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.contrib.auth import login

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

#Enail
import requests
from django.http import HttpResponse
from django.views import View
from msal import PublicClientApplication

from django.views import View
from django.shortcuts import render, HttpResponse, redirect
from msal import PublicClientApplication
import requests

from .models import Usuario

from django.shortcuts import render, redirect
import requests
from .forms import LoginForm
from django.views import View
from django.contrib.auth import authenticate
from django.contrib.auth import login

from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from rest_framework.response import Response


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm

"""
class EnviarCorreoOutlook(View):
    template_name = "pages/emailSuccess.html"

    def get(self, request):
        # Configura los datos de tu aplicación en Azure AD
        client_id = '3acebf80-2f2b-4d3b-9858-5e63ec6371bf'
        client_secret = 'yvZ8Q~kEmWKP5SzSEjXVRUX550j19mg_OrlxMaZL'
        tenant_id = 'dcec6cc1-cc36-4bdf-a82c-eaddb2de00ea'

        # Configura la URL de autorización y token
        auth_url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'

        # Datos del usuario o dirección de correo
        user_email = 'ljmdlc31@gmail.com'

        # Configura el contenido del correo
        correo = {
            'message': {
                'subject': 'Asunto del correo',
                'body': {
                    'contentType': 'Text',
                    'content': 'Contenido del correo'
                },
                'toRecipients': [{'emailAddress': {'address': user_email}}]
            }
        }

        # Solicita un token de acceso
        token_data = {
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'scope': 'https://graph.microsoft.com/.default',
            'client_secret': client_secret
        }

        token_response = requests.post(auth_url, data=token_data)
        token = token_response.json().get('access_token')

        if token:
            # Envía el correo utilizando la API de Microsoft Graph
            correo_url = 'https://graph.microsoft.com/v1.0/me/sendMail'
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }

            response = requests.post(correo_url, headers=headers, json=correo)

            if response.status_code == 202:
                envio_exitoso = True
                mensaje = 'Correo enviado correctamente'
            else:
                envio_exitoso = False
                mensaje = 'Error al enviar el correo'

            context = {
                'envio_exitoso': envio_exitoso,
                'mensaje': response.text,
            }

            return render(request, self.template_name, context)
        else:
            envio_exitoso = False
            mensaje = 'Error al obtener el token'
            context = {
                'envio_exitoso': envio_exitoso,
                'mensaje': mensaje,
            }

            return render(request, self.template_name, context)
"""
class EnviarCorreoOutlook(View):
  template_name = "pages/emailSuccess.html"
  def get(self, request):        
      
      try:
          subject = 'Registro exitoso TESCHI ISCS'
          message = 'Hola esto es un envio de correo'
          from_email = settings.EMAIL_HOST_USER
          recipient_list = ['2019452092@teschi.edu.mx','ljmdlc31@gmail.com']
          
          send_mail(subject, message, from_email, recipient_list)
          
          
          envio_exitoso = True
          mensaje = 'Correo enviado'
          context = {
              'envio_exitoso': envio_exitoso,
              'mensaje': mensaje,
          }
          return render(request, self.template_name, context)             
      except Exception as e:
          envio_exitoso = False
          context = {
              'envio_exitoso': envio_exitoso,
              'mensaje': e,
          }
          return render(request, self.template_name, context)

"""
class EnviarCorreoOutlook(View):
    template_name = "pages/emailSuccess.html"
    def get(self, request):        
        # Datos de la aplicación registrada en Azure AD
        client_id = '3acebf80-2f2b-4d3b-9858-5e63ec6371bf'
        client_secret = 'yvZ8Q~kEmWKP5SzSEjXVRUX550j19mg_OrlxMaZL'
        tenant_id = 'dcec6cc1-cc36-4bdf-a82c-eaddb2de00ea'
        
        # URL de autorización y token
        auth_url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'
        
        # Datos del usuario (puede obtenerse a través de autenticación en tu aplicación)
        user_email = 'ljmdlc31@gmail.com'  # Reemplaza con el correo del usuario
        
        # Contenido del correo
        correo = {
            'message': {
                'subject': 'Correo de prueba',
                'body': {
                    'contentType': 'Text',
                    'content': 'Esto es un correo de prueba enviado desde Django'
                },
                'toRecipients': [{'emailAddress': {'address': user_email}}]
            }
        }
        
        # Solicitar un token de acceso
        token_data = {
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'scope': 'https://graph.microsoft.com/.default',
            'client_secret': client_secret
        }
        token_response = requests.post(auth_url, data=token_data)
        token = token_response.json().get('access_token')
        
        if token:
            # Enviar el correo utilizando la API de Microsoft Graph
            correo_url = 'https://graph.microsoft.com/v1.0/me/sendMail'
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
            response = requests.post(correo_url, headers=headers, json=correo)
            
            if response.status_code == 202:
                envio_exitoso = True
                mensaje = 'Correo enviado correctamente'                
            else:
                envio_exitoso = False
                mensaje = 'Error al enviar el correo'   
            context = {
              'envio_exitoso': envio_exitoso,
              'mensaje': response.text,
            }             
            return render(request, self.template_name, context)
        else:
            envio_exitoso = False
            mensaje = 'Error al obtener el token'   
            context = {
              'envio_exitoso': envio_exitoso,
              'mensaje': mensaje,
            }             
            return render(request, self.template_name, context)
"""



class IniciarSesion(APIView):
    template_name = "accounts/login.html"

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            contraseña = form.cleaned_data['contraseña']
            usuario = authenticate(request, username=email, password=contraseña)

            if usuario is not None:
                login(request, usuario)
                # Redirige a la página de inicio o a donde desees después del inicio de sesión
                return redirect('pages/index.html')
            else:
                # El inicio de sesión falló, muestra un mensaje de error en la plantilla
                form.add_error(None, 'Las credenciales de inicio de sesión son incorrectas.')

        # Renderiza la página de inicio de sesión nuevamente con los errores
        return render(request, "accounts/login.html", {'form': form})


class RegistroUsuarioView:
    def crear_usuario(request):
        if request.method == 'POST':
            # Obtén los datos del formulario (esto puede variar según tu formulario)
            nombre = request.POST['nombre']
            correo = request.POST['correo']
            contraseña = request.POST['contraseña']

            # Crea una instancia del modelo Usuario con los datos
            nuevo_usuario = Usuario(nombre=nombre, correo=correo, contraseña=contraseña)

            # Guarda el nuevo usuario en la base de datos
            nuevo_usuario.save()

            # Redirige a una página de éxito o donde desees
            #return redirect('accounts/login.html')
            EnviarCorreo().enviar_correo(nombre, correo, contraseña)

            # Redirige a una página de éxito o donde desees
            return redirect('accounts/login.html')
        else:
            return render(request, 'accounts/register.html')  # Renderiza el formulario de registro en el método GET

class EnviarCorreo(APIView):
    def enviar_correo(self, nombre, correo, contraseña):        
        try:
            
            subject = 'Registro exitoso TESCHI ISCS'
            message = f'Hola {nombre}, ¡tu registro en la aplicación TESCHI ISCS ha sido exitoso!, tus datos para iniciar sesión son: Nombre: {nombre} Contraseña: {contraseña}'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [correo]
            
            send_mail(subject, message, from_email, recipient_list)
            
        except Exception as e:
            print(f"Error al enviar el correo: {str(e)}")
            pass


# Create your views here.
class Home(APIView):
    template_name = "accounts/login.html"
    def get(self, request):
        return render(request, self.template_name)

class redireccionarIndex(APIView):
    template_name = "pages/index.html"
    def get(self, request):
        # Lógica para renderizar la página 'index.html' en una solicitud GET
        return render(request, self.template_name)

    def post(self, request):
        # Lógica para procesar la solicitud POST
        # Puedes redirigir o realizar otras acciones aquí
        # Por ejemplo, redirigir al usuario a otra página después de un formulario POST
        return redirect('redireccionarIndex')  # Asegúrate de que 'otra_pagina' sea el nombre de una vista en tu urls.py

class LoginView(APIView):
    template_name = "pages/login.html"  # Asegúrate de que el nombre de la plantilla sea correcto

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            # Procesa los datos del formulario aquí
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Agrega tu lógica de autenticación aquí
            # Por ejemplo, verifica las credenciales del usuario

            # Luego puedes redirigir al usuario a la página de inicio u otra página
            return redirect('redireccionarIndex')  # Asegúrate de definir 'inicio' en tus URLs

        return render(request, self.template_name, {'form': form})
    
# Django plantilla



# Create your views here.

def index(request):
  return render(request, 'pages/index.html')

def typography(request):
  return render(request, 'pages/typography.html')

def color(request):
  return render(request, 'pages/color.html')

def icon_tabler(request):
  return render(request, 'pages/icon-tabler.html')

def sample_page(request):
  return render(request, 'pages/sample-page.html')

def alta_alumnos(request):
  return render(request, 'pages/alta_alumnos.html')

def alta_profesores(request):
  return render(request, 'pages/alta_profesoses.html')

def alta_materias(request):
  return render(request, 'pages/alta_materias.html')


# Authentication
def registration(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      print('Account created successfully!')
      nombre = form.cleaned_data['username']
      correo = form.cleaned_data['email']
      contraseña = form.cleaned_data['password1']
      EnviarCorreo().enviar_correo(nombre, correo, contraseña)
      return redirect('/accounts/login/')
    else:
      print("Registration failed!")
  else:
    form = RegistrationForm()
  
  context = {'form': form}
  return render(request, 'accounts/register.html', context)

class UserLoginView(auth_views.LoginView):
  template_name = 'accounts/login.html'
  form_class = LoginForm
  success_url = '/'

class UserPasswordResetView(auth_views.PasswordResetView):
  template_name = 'accounts/password_reset.html'
  form_class = UserPasswordResetForm

class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
  template_name = 'accounts/password_reset_confirm.html'
  form_class = UserSetPasswordForm

class UserPasswordChangeView(auth_views.PasswordChangeView):
  template_name = 'accounts/password_change.html'
  form_class = UserPasswordChangeForm

def user_logout_view(request):
  logout(request)
  return redirect('/accounts/login/')

