from django.contrib import admin
from .models import Categorias, Proveedores, Productos, Clientes, Empleados, FacturaVentas, DetalleVentas, Movimientos

admin.site.register(Categorias)
admin.site.register(Proveedores)
admin.site.register(Productos)
admin.site.register(Clientes)
admin.site.register(Empleados)
admin.site.register(FacturaVentas)
admin.site.register(DetalleVentas)
admin.site.register(Movimientos)
