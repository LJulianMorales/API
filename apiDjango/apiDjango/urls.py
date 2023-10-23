"""apiDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import Home, redireccionarIndex, LoginView #,microsoft_profile

from django.urls import path, re_path, include
from api import views

from django.contrib.auth import views as auth_views
#from social_django.views import auth, complete


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", LoginView.as_view(), name="login"),
    path('redireccionarIndex/', redireccionarIndex.as_view(), name='redireccionarIndex'),
    path('accounts/login', LoginView.as_view(), name='login'),

    path('typography/', views.typography, name='typography'),
    path('color/', views.color, name='color'),
    path('icon-tabler/', views.icon_tabler, name='icon_tabler'),
    path('sample-page/', views.sample_page, name='sample_page'),
    path('alumnos/', views.alta_alumnos, name='alta_alumnos'),
    path('profesores/', views.alta_profesores, name='alta_profesores'),
    path('emailSuccess/', views.EnviarCorreoOutlook.as_view(), name='enviar_correo'),

    path('', views.EnviarCorreo.as_view(), name='enviar_correo'),

    #path('pages/profile-info/', microsoft_profile.as_view(), name='microsoft_profile'),
    #path('login/microsoft/', auth, name='auth_login_microsoft'),
    #path('complete/microsoft/', complete, name='complete_microsoft'),
    path('accounts/solicitud_alta/',  views.solicitud_alta, name='solicitud_alta'),

    path('',  views.executeFunction, name='execute'),

    path('auth/microsoft/login/', views.microsoft_login, name='microsoft_login'),
    path('auth/microsoft/callback/', views.microsoft_callback, name='microsoft_callback'),

    path('alumnos/', views.registrar_usuario, name='registrar_usuario'),    
    path('google/',views.GoogleSheetsAPIView.as_view(), name='google'),
    # path('consulta/',views.consulta, name='consulta'),
    path('consulta_respuestas/<int:cuestion>/', views.consulta_respuestas, name='consulta_respuestas'),
    

    

    # Authentication
    path('accounts/login/', views.UserLoginView.as_view(), name='login'),
    path('accounts/logout/', views.user_logout_view, name='logout'),
    path('accounts/register/', views.registration, name='register'),
    path('accounts/password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'
    ), name="password_change_done" ),
    path('accounts/password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('accounts/password-reset-confirm/<uidb64>/<token>/', 
        views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),
]



