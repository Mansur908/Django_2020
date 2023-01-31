from django import forms
from django.forms import ModelForm
from django.forms.widgets import Input

from users.models import Air_ticket


class TablesForm(forms.Form):
    table = forms.CharField()

class CarNameForm(forms.Form):
    name = forms.CharField()

class CarPriceForm(forms.Form):
    price = forms.CharField()

class AddTicketForm(ModelForm):
    class Meta:
        model = Air_ticket
        fields = ["departure_place","arrival_place","date","price","air_company"]

        widgets = {
            "departure_place": Input(attrs={
                'type': "text",
                'name': "departure_place",
                'class': "e1",
                'placeholder': "departure_place"
            }),
            "arrival_place": Input(attrs={
                'type': "text",
                'name': "arrival_place",
                'class': "e2",
                'placeholder': "arrival_place"
            }),
            "date": Input(attrs={
                'type': "date",
                'name': "date",
                'class': "e2",
                'placeholder': "date"
            })
            ,
            "price": Input(attrs={
                'type': "text",
                'name': "price",
                'class': "e2",
                'placeholder': "price"
            }),
            "air_company": Input(attrs={
                'type': "text",
                'name': "air_company",
                'class': "e2",
                'placeholder': "air_company",
            })
        }