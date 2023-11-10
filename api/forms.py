from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

# Django template
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UsernameField, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Contraseña"),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg', 
            'placeholder': 'Contraseña'
        }),
    )
    password2 = forms.CharField(
        label=_("Confirmar contraseña"),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg', 
            'placeholder': 'Confirmar contraseña'
        }),
    )

    class Meta:
        model = User
        fields = ('username', 'email', )

        widgets = {
        'username': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre de usuario'
        }),
        'email': forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Correo'
        })
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Username"
    }))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password", 
            "class": "form-control",
            "placeholder": "Password"
        }),
    )

class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "Email"
    }))

class UserSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        "placeholder": "New Password"
    }), label="New Password")
    new_password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        "placeholder": "Confirm New Password"
    }), label="Confirm New Password")
    

class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        "placeholder": "Old Password"
    }), label='Old Password')
    new_password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        "placeholder": "New Password"
    }), label="New Password")
    new_password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        "placeholder": "Confirm New Password"
    }), label="Confirm New Password")

"""
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('enrollment', 'account_id', 'first_name', 'last_name', 'middle_name', 'curp', 'nss', 'phone', 'mobile')

    widgets = {
        'enrollment': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enrollment'
        }),
        'account_id': forms.Select(attrs={
            'class': 'form-control',
        }),
        'first_name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First Name'
        }),
        'last_name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last Name'
        }),
        'middle_name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Middle Name'
        }),
        'curp': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'CURP'
        }),
        'nss': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'NSS'
        }),
        'phone': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Phone'
        }),
        'mobile': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Mobile'
        }),
    }
"""

from django import forms
from .models import Account

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['email', 'type_user_id']


class alumnForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['enrollment', 'first_name', 'last_name', 'middle_name', 'curp', 'nss', 'phone', 'mobile']
