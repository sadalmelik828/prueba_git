from django.db import models
from django_app.f1.models import Municipio

class Editor(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=60)
    departamento = models.CharField(max_length=40)
    pais = models.CharField(max_length=50)
    web = models.URLField(blank=True, verbose_name='pagina web', help_text="Por favor escriba la direccion junto con el http://")

    def __unicode__(self):
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(blank=True, verbose_name="correo electronico")

    def __unicode__(self):
        return u'%s %s' % (self.nombre, self.apellido)

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autores = models.ManyToManyField(Autor)
    editor = models.ForeignKey(Editor)
    fecha_publicacion = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.titulo

class Tienda(models.Model):
    nombre = models.CharField(max_length=50)
    municipio = models.ForeignKey(Municipio)
    direccion = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre