from django.contrib import admin
from .models import Cliente, Empleado

admin.site.register(Cliente)
admin.site.register(Empleado)
# Register your models here.

##Si aca coloco cliente pero en los modelos debe de ser plurar, en el admin me sale con doble SS?

