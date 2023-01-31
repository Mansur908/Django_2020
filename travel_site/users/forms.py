import json

from django import forms
from django.forms.widgets import Input
from .models import Person, Message
from django.forms import ModelForm, TextInput, FileInput, Textarea, FileField, CharField


class SignInForm(ModelForm):
    class Meta:
        model = Person
        fields = ['email','password']

        widgets = {
            "email": Input(attrs={
                'type': "email",
                'placeholder':'email',
                'class': 'name'
            }),
            "password": Input(attrs={
                'type': "password",
                'class': 'password_log',
                'placeholder': 'password'
            })
        }

class SignUpForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name','email','password']

        widgets = {
            "name": TextInput(attrs={
                'placeholder': 'username',
                'class': 'name'
            }),
            "email": Input(attrs={
                'type':"email",
                'placeholder':'email',
                'class': 'email'
            }),
            "password": Input(attrs={
                'type': "password",
                'class': 'password',
                'placeholder': 'password'
            })
        }

class ImageForm(ModelForm):
    class Meta:
        model = Person
        fields = ['picture']


        widgets = {
            "picture": FileInput(attrs={
                'type': "file",
                'name': "file"
            })
        }

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['text']

        widgets = {
            "text": Textarea(attrs={
                'class': 'coment',
                'name': "text",
                'placeholder': "Enter Message"
            })
        }

