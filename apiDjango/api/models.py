from django.db import models
from django.contrib.sessions.models import Session

class UserType(models.Model):
    type_user_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50, default='')

class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50, default='')
    password = models.CharField(max_length=30, default='')
    type_user_id = models.ForeignKey(UserType, on_delete=models.CASCADE)

class CustomUser(models.Model):
    enrollment = models.AutoField(primary_key=True)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    middle_name = models.CharField(max_length=30, default='')
    curp = models.CharField(max_length=30, unique=True, default='')
    nss = models.CharField(max_length=30, unique=True, default='')
    phone = models.CharField(max_length=30, default='')
    mobile = models.CharField(max_length=30, default='')

class CustomSession(models.Model):
    session = models.OneToOneField(Session, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, null=True, blank=True, on_delete=models.CASCADE)    


class Pregunta(models.Model):
    description = models.TextField(max_length=100)

class Respuesta(models.Model):
    cuestion = models.IntegerField()
    response = models.TextField()