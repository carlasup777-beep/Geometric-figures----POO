from django.db import models

# Create your models here.

class Domicilio(models.Model):
    calle = models.CharField(max_length=70)
    no_calle = models.IntegerField()
    pais = models.CharField(max_length=60)

    def __str__(self):
        return F'Domicilio {self.id} {self.calle} {self.no_calle} {self.pais})'

class Persona(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()
    edad = models.IntegerField()
    SEXO_CHOICES = ('M', 'Masculino'), ('F', 'Femenino')
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)

    dom = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True) #Si se borra la tabla o registro, se reemplazara con Null
    # dom = models.ForeignKey(Domicilio, on_delete=models.CASCADE, null=True) #Borra todo el registro

    def __str__(self):
        return F'Persona {self.id} {self.nombre} {self.apellido} {self.edad})'

