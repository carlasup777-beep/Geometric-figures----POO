from django.forms import modelform_factory
from django.shortcuts import render, redirect
from persona.models import Persona

# Create your views here.
def detallePer (request, id):
    personas = Persona.objects.get(pk=id)
    return render(request, 'personas/detalle.html', {'persona': personas})

PersonaForm = modelform_factory(Persona, exclude=[])

def nuevapersona(request):
    if request.method == "POST": #Segunda Fase
        FormaPersona = PersonaForm(request.POST)
        if FormaPersona.is_valid():
            FormaPersona.save()
            return redirect('home')
        else:
            return render(request, 'personas/nuevo.html', {'FormPersona': FormaPersona})
    else: #Primera fase
        FormaPersona = PersonaForm()  # crear instancia de PersonaForm vacio (Formulario)
        return render(request, 'personas/nuevo.html', {'FormPersona': FormaPersona})
