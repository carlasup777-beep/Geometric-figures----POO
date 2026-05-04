from django.forms import modelform_factory
from django.shortcuts import render
from persona.models import Persona

# Create your views here.

def detallePer (request, id):
    personas = Persona.objects.get(pk=id)
    return render(request, 'personas/detalle.html', {'persona': personas})

PersonaForm = modelform_factory(Persona, exclude=[])
def nuevapersona(request):
    FormaPersona=  PersonaForm() #crear instancia de PersonaForm (Formulario)
    return render(request, 'personas/nuevo.html', {'FormaPersona': FormaPersona})

