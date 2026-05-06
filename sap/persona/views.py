from django.forms import modelform_factory
from django.shortcuts import render, redirect
from persona.models import Persona
from persona.models import Domicilio


# Create your views here.
def detallePer (request, id):
    personas = Persona.objects.get(pk=id)
    return render(request, 'personas/detalle.html', {'persona': personas})

PersonaForm = modelform_factory(Persona, exclude=[])
DomForm = modelform_factory(Domicilio, exclude=[])

def newDom(request):
    if request.method == 'POST':
        form = DomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return redirect('home')

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

def eliminarPersona(request, id):
    persona = Persona.objects.get(pk=id)
    if request.method == "POST":
        persona.delete()
        return redirect('home')
    return render(request, 'personas/BorrarP.html', {'persona': persona})

def editarPer(request, id):
    if request.method == "POST":
        persona = Persona.objects.get(pk=id)
        FormaPersona = PersonaForm(request.POST, instance=persona)
        if FormaPersona.is_valid():
            FormaPersona.save()
            return redirect('home')
        else:
            return render(request, 'personas/nuevo.html', {'FormPersona': FormaPersona})
    else: #Metodo GET
        persona = Persona.objects.get(pk=id)
        FormaPersona = PersonaForm(instance=persona)  # crear instancia de PersonaForm vacio (Formulario)
        return render(request, 'personas/nuevo.html', {'FormPersona': FormaPersona})