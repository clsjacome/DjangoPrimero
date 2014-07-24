# -*- coding: utf-8 -*-
#Se utiliza esa primera línea para especificar el encoding del documento
__author__ = 'jacome'

from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label="Tu correo electrónico")
    message = forms.CharField(widget=forms.Textarea)
    #Por si se necista validar de forma específica un campo
    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message
