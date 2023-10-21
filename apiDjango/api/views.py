from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import render, redirect
from api.forms import LoginForm 

#Django plantilla
from django.shortcuts import render, redirect
from api.forms import LoginForm, RegistrationForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.contrib.auth import login

from django.contrib.auth import authenticate, login

#Enail
from django.views import View

from .forms import LoginForm
from django.views import View
from django.contrib.auth import authenticate
from django.contrib.auth import login

from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm

from django.shortcuts import render
from django.views import View

from django.shortcuts import render, redirect

from django.views import View
from django.shortcuts import render


from django.shortcuts import render, redirect
import requests
from django.conf import settings
from django.shortcuts import render, redirect
import requests
from django.conf import settings
from urllib.parse import urlencode

from django.shortcuts import render, redirect
from django.conf import settings
import requests

# ----------- Se importan los modelos ----------------

#from .models import usuario
#from .models import tipousuario
from .models import Account

def microsoft_login(request):
    authorization_url = f"{settings.AZURE_AD_AUTHORITY}/oauth2/v2.0/authorize"
    params = {
        'client_id': settings.AZURE_AD_CLIENT_ID,
        'response_type': 'code',
        'redirect_uri': settings.AZURE_AD_REDIRECT_URI,
        'response_mode': 'query',
        'scope': 'User.Read',
    }
    login_url = f"{authorization_url}?{urlencode(params)}"
    return redirect(login_url)

def microsoft_callback(request):
    code = request.GET.get('code')
    token_url = f"{settings.AZURE_AD_AUTHORITY}/oauth2/v2.0/token"
    data = {
        'client_id': settings.AZURE_AD_CLIENT_ID,
        'scope': 'User.Read',
        'code': code,
        'redirect_uri': settings.AZURE_AD_REDIRECT_URI,
        'grant_type': 'authorization_code',
        'client_secret': settings.AZURE_AD_CLIENT_SECRET,
    }
    token_response = requests.post(token_url, data=data).json()
    access_token = token_response.get('access_token')

    if access_token:
        user_info_url = 'https://graph.microsoft.com/v1.0/me'
        headers = {'Authorization': f'Bearer {access_token}'}
        user_info = requests.get(user_info_url, headers=headers).json()
        
        if 'userPrincipalName' in user_info:
            user_email = user_info['userPrincipalName']
            if findAccount(request, user_email):
                return render(request, 'pages/profile-info.html', {'user_info': user_info})
            else:
                return render(request, 'accounts/solicitud_alta.html')

    return render(request, 'accounts/login_error.html')



def findAccount(request, user_email):
    try:
        account_match = Account.objects.get(email=user_email)
        return True
    except Account.DoesNotExist:
        return False



"""
class microsoft_profile(APIView):
    template_name = "pages/profile-info.html"
    print("entro")
    def post(self, request):
        # Verifica si el usuario está autenticado
        if request.user.is_authenticated:
            try:
                # Obtiene los detalles del perfil del usuario desde las redes sociales (Azure AD)
                social = UserSocialAuth.objects.get(user=request.user, provider='azuread-oauth2')
                social_data = social.extra_data
                user_email = social_data.get('userPrincipalName')
                display_name = social_data.get('displayName')

                # Comprueba si los datos requeridos están disponibles
                if user_email and display_name:
                    return render(request, self.template_name, {
                        'user_email': user_email,
                        'display_name': display_name,
                    })

            except UserSocialAuth.DoesNotExist:
                pass

        # Si el usuario no está autenticado o faltan datos, puedes redirigirlo a la página de inicio de sesión
        return redirect(reverse('auth_login_microsoft'))  # Utiliza el nombre de URL definido en tus rutas URL
"""


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
"""
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
        GoogleSheetsAPIView()
        return render(request, self.template_name)

    def post(self, request):
        # Lógica para procesar la solicitud POST
        # Puedes redirigir o realizar otras acciones aquí
        # Por ejemplo, redirigir al usuario a otra página después de un formulario POST
        return redirect('redireccionarIndex')  # Asegúrate de que 'otra_pagina' sea el nombre de una vista en tu urls.py

class LoginView(APIView):
    template_name = "accounts/login.html"  

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

def solicitud_alta(request):
  return render(request, 'accounts/solicitud_alta.html')


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

from .models import Account, CustomUser, UserType
from django.http import JsonResponse

def executeFunction(request):
    """
    # Crear una instancia de Account primero
    
    userType = UserType(description='Administrador')
    userType.save()
    userType = UserType(description='Docente')
    userType.save()
    userType = UserType(description='Alumno')
    userType.save()
    
    # Recupera la instancia de tipousuario con id=1
    user_type = tipousuario.objects.get(tipo_usuario_id=1)

    # Crea una nueva instancia de Account y asigna la instancia de tipousuario
    account = Account(email='admin@example.com', password='1234', id_tipo_usuario=user_type)
    account.save()
    
    account_id = Account.objects.get(id=1)

    # Luego, crear una instancia de CustomUser y asignarle la instancia de Account
    custom_user = usuario(enrollment='00000000', account_id=account_id, first_name='Admin')
    custom_user.save()
    """

    try:
        # Realiza las operaciones necesarias en tu función de Python aquí
        # ...

        return JsonResponse({'status': 'success'})  # Devuelve una respuesta JSON
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})

# -------------------- Vistas de registro -----------------------

from django.shortcuts import render, redirect
from .models import Account, CustomUser, UserType, Pregunta, Respuesta
from .forms import alumnForm, AccountForm 
import secrets
import string

def generate_password():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(8))
    return password
"""
def registrar_usuario(request):

    print("Entro")
    if request.method == 'POST':

        account_form = AccountForm(request.POST) 
        custom_user_form = alumnForm(request.POST)

        if account_form.is_valid() and custom_user_form.is_valid():

            # Extrae los datos del formulario
            matricula = custom_user_form.cleaned_data['enrollment']
            type_user_id_value = custom_user_form.cleaned_data['type_user_id']

            email = f'{matricula}@teschi.edu.mx'
            password = generate_password()

            # Intenta crear una instancia de Account
            try:
                user_type = UserType.objects.get(id=type_user_id_value)
                account = Account(email=email, password=password, type_user_id=user_type)
                account.save()

                # Si se ha creado con éxito, usa el account_id para crear un CustomUser
                custom_user = CustomUser(enrollment=matricula, 
                                         account_id=account, 
                                         first_name=custom_user_form.cleaned_data['first_name'],
                                         last_name=custom_user_form.cleaned_data['last_name'],
                                         middle_name=custom_user_form.cleaned_data['middle_name'],
                                         curp=custom_user_form.cleaned_data['curp'],
                                         nss=custom_user_form.cleaned_data['nss'],
                                         phone=custom_user_form.cleaned_data['phone'],
                                         mobile=custom_user_form.cleaned_data['mobile'])
                custom_user.save()
                usuario_creado = "El usuario se creó con éxito"
                EnviarCorreo().enviar_correo(custom_user_form.cleaned_data['first_name'], email, password)
                return JsonResponse({'status': 'success'})
            except UserType.DoesNotExist:                
                return JsonResponse({'status': 'error'})
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)})

    else:
        return JsonResponse({'status': 'error'})

    context = {
        'account_form': account_form,
        'custom_user_form': custom_user_form,
        'usuario_creado': usuario_creado,  # Pasa el mensaje a la plantilla
    }

    return JsonResponse({'status': 'error'})

"""


import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect


def registrar_usuario(request):
    print("Entro")
    if request.method == 'POST':
        # Asegúrate de que el contenido de la solicitud sea JSON
        if request.content_type == 'application/json':
            try:
                data = json.loads(request.body.decode('utf-8'))  # Analiza los datos JSON

                matricula = data.get('enrollment')
                type_user_id_value = data.get('type_user_id')

                email = f'{matricula}@teschi.edu.mx'
                password = generate_password()

                # Intenta crear una instancia de Account
                try:
                    user_type = UserType.objects.get(id=type_user_id_value)
                    account = Account(email=email, password=password, type_user_id=user_type)
                    account.save()

                    # Si se ha creado con éxito, usa el account_id para crear un CustomUser
                    custom_user = CustomUser(enrollment=matricula,
                                             account_id=account,
                                             first_name=data.get('first_name'),
                                             last_name=data.get('last_name'),
                                             middle_name=data.get('middle_name'),
                                             curp=data.get('curp'),
                                             nss=data.get('nss'),
                                             phone=data.get('phone'),
                                             mobile=data.get('mobile'))
                    custom_user.save()
                    return JsonResponse({'status': 'success', 'message': 'Usuario registrado'})
                except UserType.DoesNotExist:
                    return JsonResponse({'status': 'error', 'message': 'El tipo de usuario no existe'})
                except Exception as e:
                    return JsonResponse({'status': 'error', 'message': str(e)})
            except json.JSONDecodeError:
                return JsonResponse({'status': 'error', 'message': 'Datos JSON inválidos'})

    return JsonResponse({'status': 'error', 'message': 'Error que aun no compruebo'})

from google.oauth2 import service_account
import gspread
from rest_framework.response import Response
"""
class GoogleSheetsAPIView(APIView):
    def get(self, request):
        # Ruta al archivo de credenciales JSON
        credentials_file = "api/templates/credentials/django-402605-a2f85ac7560a.json"
        # Configura las credenciales utilizando google-auth
        scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
        credentials = service_account.Credentials.from_service_account_file(
            credentials_file, scopes=scopes
        )

        # Autentica con Google Sheets
        gc = gspread.Client(auth=credentials)
        gc.session.verify = True  # Esto habilita la verificación SSL

        # Abre la hoja de cálculo por su URL o nombre
        spreadsheet = gc.open("ControlEscolarISCS")

        # Accede a las hojas y realiza las operaciones necesarias
        worksheet = spreadsheet.worksheet("RespuestasFORM")

        # Realiza operaciones en la hoja de cálculo, como leer datos
        data = worksheet.get_all_records()
        # Procesa los datos y realiza las acciones necesarias

        Response.objects.all().delete()
        print(data)

        return Response({"Datos de Google Sheets": data})"""
    
from django.shortcuts import get_object_or_404
class GoogleSheetsAPIView(APIView):
    def get(self, request):
        # Ruta al archivo de credenciales JSON
        credentials_file = "api/templates/credentials/django-402605-a2f85ac7560a.json"
        # Configura las credenciales utilizando google-auth
        scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
        credentials = service_account.Credentials.from_service_account_file(
            credentials_file, scopes=scopes
        )

        # Autentica con Google Sheets
        gc = gspread.Client(auth=credentials)
        gc.session.verify = True  # Esto habilita la verificación SSL

        # Abre la hoja de cálculo por su URL o nombre
        spreadsheet = gc.open("ControlEscolarISCS")

        # Accede a las hojas y realiza las operaciones necesarias
        worksheet = spreadsheet.worksheet("RespuestasFORM")

        # Realiza operaciones en la hoja de cálculo, como leer datos
        data = worksheet.get_all_records()
        
        # Borra los registros anteriores en el modelo Respuesta
        Respuesta.objects.all().delete()

        # Itera a través de los datos y almacena las respuestas en el modelo Respuesta
        for entry in data:
            for pregunta, respuesta in entry.items():
                if pregunta == "Marca temporal" or pregunta == "Dirección de correo electrónico":
                    continue

                # Depuración: Agregar impresiones
                print(f"Pregunta: {pregunta}, Respuesta: {respuesta}")

                # Busca la pregunta en el modelo Cuestion por descripción
                _cuestion = get_object_or_404(Pregunta, description=pregunta)
                _id = int(_cuestion.pk)

                # Crea un nuevo objeto Response con el id de la pregunta y la respuesta
                _response = Respuesta(cuestion=_id, response=respuesta)
                _response.save()

        return Response({"Datos de Google Sheets": data})
