# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="roque"
__date__ ="$21/07/2010 05:15:17 PM$"

from django.contrib import admin
from django_app.libros.models import Editor, Autor, Libro

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email')
    #list_display_links = ('nombre', 'apellido')
    search_fields = ('nombre', 'apellido')

class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'editor', 'fecha_publicacion')
    list_filter = ('fecha_publicacion',)
    date_hierarchy = 'fecha_publicacion'
    ordering = ('-fecha_publicacion',)
    #fields = ('titulo', 'editor', 'autores', 'fecha_publicacion')
    filter_horizontal = ('autores',)
    #raw_id_fields = ('editor',)
    #radio_fields = {"editor": admin.VERTICAL}

admin.site.register(Editor)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)