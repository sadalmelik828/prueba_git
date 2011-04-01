# Create your views here.

from django.core.mail import send_mail
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django_app.libros.forms import ContactoForm
from django_app.libros.models import Libro

def busqueda(request):
    return render_to_response('form_busqueda.html')

def res_busqueda(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            libros = Libro.objects.filter(titulo__icontains=q)
            return render_to_response('form_busqueda.html', {'libros': libros, 'consulta': q})
    return render_to_response('form_busqueda.html', {'error': error})
    
def visualiza_meta(request):
    valores = request.META.items()
    valores.sort()
    return render_to_response('meta.html', {'valores': valores})

def contacto(request):    
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            cd = formulario.cleaned_data
            opc = request.POST['opciones'].itervalues()
            #r = ', '.join(opc)
            send_mail(
                      cd['asunto'],
                      cd['mensaje'],
                      cd.get('email', 'noresponder@ejemplo.com'),
                      ['sadalmelik828@gmail.com'],
                      )
            return HttpResponseRedirect('/hora/'+opc)
    else:
        formulario = ContactoForm(
        initial={'asunto': 'Me gusta tu sitio!'}
        )
    return render_to_response('form_contacto.html', { 'formulario': formulario })
