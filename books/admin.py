__author__ = 'jacome'
#Registrar los models para que se vean en la interfaz de admin

from django.contrib import admin
from books.models import Publisher, Author, Book

#=========Model admins para cotsumizar la interfaz de admin de cada model================================
class AuthorAdmin(admin.ModelAdmin):
    #---Change List
    #list_display para especificar las cols a mostrar
    list_display = ('first_name', 'last_name', 'email')
    #search_fields crea una barra buscadora. Especificar los campos que se van a buscar
    search_fields = ('first_name', 'last_name')

    #--Edit Forms


class BookAdmin(admin.ModelAdmin):
    #--Change List
    list_display = ('title', 'publisher', 'publication_date')
    #list_filter agrega un filtro en la parte izquierda del sitio
    list_filter = ('publication_date','publisher')

    #--Edit Forms
    #Crea una lista del campo
    filter_horizontal = ('authors',)
    #Despliga un TB en vez de un CB
    raw_id_fields = ('publisher',)


#===================Registrar los models en admin========================================================
#Ojo: especificar el ModelAdmin si se va a utilizar uno
admin.site.register(Publisher)
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)