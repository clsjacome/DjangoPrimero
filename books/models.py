# -*- coding: utf-8 -*-
#Se utiliza esa primera línea para especificar el encoding del documento

#Archivo donde crear los models. Un model es una tabla de la base de datos. Cada atributo es una columna de la tabla
from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    def __unicode__(self):
        #Para que se muestre lo del metodo en print y en admin
        return self.name
    class Meta: #Especificar varios valores utilesdel modelo
        ordering = ['name']

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    #verbose_name se utiliza verbose_name para especificar el nombre del campo en el admin site
    #blank=True para admitir vacios (no nulls)
    email = models.EmailField(blank=True, verbose_name='Correo Electrónico')

    def __unicode__(self):
        return u'%s %s' %(self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    #Para admitir una fecha (o un valor numerico) en blanco se deben usar los dos, blank y null
    publication_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return  self.title