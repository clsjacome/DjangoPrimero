# -*- coding: utf-8 -*-
#Se utiliza esa primera línea para especificar el encoding del documento
from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book

# Create your views here.
def search_form(request):
    return render(request, 'search_form.html',{'error':False})

def search(request):
    #Checar que si haya sido pasado un parametro q
    isSubmitted = 'q' in request.GET
    if isSubmitted and request.GET['q']: #request.GET['q'] para checar que q no esté vacío
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render(request, 'search_results.html',{'books': books, 'query': q})
    else:
       return render(request, 'search_form.html',{'error':True})