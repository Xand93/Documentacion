from django.db import models

class Registro(Models.Model):
    fecha = models.DateField('Dia', auto_now= True, auto_now_add=False)
    nombre = models.CharField(max_length = 50, blank = False, null = False)
    apellido = models.CharField(max_length = 50, blank = False, null = False)
    dni = models.IntegerField(max_length = 50, blank = False, null = False)
    tarea = models.CharField(max_length = 50, blank = False, null = False)
    cliente = models.CharField(max_length = 50, blank = False, null = False)
