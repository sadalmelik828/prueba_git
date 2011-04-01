# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__ = "roque"
__date__ = "$14/08/2010 04:20:59 PM$"

from django import forms
from django.forms import ModelForm, CheckboxSelectMultiple

CHOICES = (
	(1, 'uno'),
	(2, 'dos'),
	(3, 'tres'),
	(4, 'cuatro'),
	(5, 'cinco'),
	)

class ContactoForm(forms.Form):
    asunto = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label='Correo')
    mensaje = forms.CharField(widget=forms.Textarea)
    opciones = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=CHOICES)

    def clean_mensaje(self):
        mensaje = self.cleaned_data['mensaje']
        num_palabras = len(mensaje.split())
        if num_palabras < 4:
            raise forms.ValidationError("No son suficientes palabras!")
        return mensaje
