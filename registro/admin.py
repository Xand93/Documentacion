from django.contrib import admin

from registro.models import Registro

class RegistroAdmin(admin.ModelAdmin):
    fields = ['fecha','nombre','apellido','dni','tarea','cliente']
admin.site.register(Registro,RegistroAdmin)



