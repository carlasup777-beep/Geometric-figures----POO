from django.contrib import admin
from django.urls import path
from webapp.views import bienvenida
from persona.views import detallePer
from persona.views import nuevapersona

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenida/', bienvenida, name='home'),
    path('detalle_persona/<int:id>/', detallePer),
    path('bienvenida/nuevapersona/', nuevapersona),
]
