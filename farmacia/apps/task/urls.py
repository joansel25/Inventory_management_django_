from django.urls import path, include
from rest_framework import routers
from .views import (
    CategoriaViewSet,
    ProductoViewSet,
    ProveedorViewSet,
    ClienteViewSet,
    EmpleadoViewSet,
    FacturaVentaViewSet,
    DetalleVentaViewSet,
    MovimientoViewSet
)

# Crear el router
router = routers.DefaultRouter()
router.register(r'categorias', CategoriaViewSet, basename='categoria')
router.register(r'productos', ProductoViewSet, basename='producto')
router.register(r'proveedores', ProveedorViewSet, basename='proveedor')
router.register(r'clientes', ClienteViewSet, basename='cliente')
router.register(r'empleados', EmpleadoViewSet, basename='empleado')
router.register(r'facturas', FacturaVentaViewSet, basename='factura')
router.register(r'detalles', DetalleVentaViewSet, basename='detalle')
router.register(r'movimientos', MovimientoViewSet, basename='movimiento')

# Incluir todas las rutas del router bajo /api/
urlpatterns = [
    path('api/', include(router.urls)),  # Las rutas quedarán como /farmacia/api/<modelo>/
]
