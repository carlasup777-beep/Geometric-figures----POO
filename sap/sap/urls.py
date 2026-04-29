from django.contrib import admin
from django.urls import path
from webapp.views import bienvenida

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenida/', bienvenida)

]
