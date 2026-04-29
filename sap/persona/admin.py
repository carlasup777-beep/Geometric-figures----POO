from django.contrib import admin
from persona.models import Persona
from persona.models import Domicilio

# Register your models here.
admin.site.register(Persona)
admin.site.register(Domicilio)