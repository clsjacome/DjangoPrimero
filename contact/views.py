# -*- coding: utf-8 -*-
#Se utiliza esa primera línea para especificar el encoding del documento
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from contact.forms import ContactForm

__author__ = 'jacome'
def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'], #El subject del mail
                request.POST['message'], #El body del mail
                request.POST.get('email', 'noreply@example.com'), #El email que aparece en from
                ['aurasoporte@gmail.com'], #La lista de los recipients
            )
            return HttpResponseRedirect('/contact/thanks/')
    return render(request, 'contactForm.html',
        {'errors': errors})

def afterMailSent(request):
    return HttpResponse("Mail Sent")

#Utilizando la libería de forms de django
def newContact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['aurasoporte@gmail.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        #initial =... para establecer los defaults
        form = ContactForm(initial={'subject':'Subject de Dfault'})
    return render(request, 'newContactForm.html', {'form': form})