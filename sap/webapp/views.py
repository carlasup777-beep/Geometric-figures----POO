from django.http import HttpResponse
from django.shortcuts import render
from persona.models import Persona

# Create your views here.
def bienvenida(request):
    # context = {'msg1':'Valor mensaje 1',
    #           'msg2':'Valor mensaje 2',
    #           'nombre':'Xavier'}
    #
    # return render(request, 'bienvenida.html', {'msg1':'Valor mensaje 1',
    #            'msg2':'Valor mensaje 2',
    #            'nombre':'Xavier'})
    # return render(request, 'bienvenida.html', context)

    cont= Persona.objects.count()
    persona = Persona.objects.all() #Read global
    return render(request, 'bienvenida.html', {'no_persona': cont, 'persona': persona})

