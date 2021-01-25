from django import forms
from django.forms import Form,PasswordInput,CharField
from django.contrib.auth.models import User



class DeliveryboyLoginForm(Form):
    username = CharField(max_length=20)
    password = CharField(widget=PasswordInput())
