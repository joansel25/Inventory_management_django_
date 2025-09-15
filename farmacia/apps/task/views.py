from rest_framework import viewsets, filters #es un modulo de django que te permite crear vistas para Apis de manera rapida y con menos codigo
from django_filters.rest_framework import DjangoFilterBackend

from .models import(
    Categoria, Producto, Proveedor,
    Cliente, Empleado, FacturaVenta,
    DetalleVenta, Movimiento
)
from .serializers import(
    CategoriaSerializer, ProductoSerializer, ProveedorSerializer,
    ClienteSerializer, EmpleadoSerializer, FacturaVentaSerializer,
    DetalleVentaSerializer, MovimientoSerializer
)
#ModeViewset  es una clase que proporciona automaticamente
#  todas las operaciones CRUD para un modelo de django

class CategoriaViewset(viewsets.ModelViewSet):
    queryset= Categoria.objects.all() #Define qué datos se van a mostrar o manipular.
    serializer_class = CategoriaSerializer #indica qué serializador usar para convertir los datos del modelo a JSON
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['nombre']
    search_fields = ['nombre']
    ordering_fields = ['id', 'nombre'] 

class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['nombre', 'precio', 'stock', 'id_categoria', 'id_proveedor']
    search_fields = ['nombre']
    ordering_fields = ['id', 'nombre', 'precio', 'stock']

class ProveedorViewset(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['nombre', 'contacto']
    search_fields = ['nombre', 'contacto']
    ordering_fields = ['id', 'nombre']

class ClienteViewset(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['nombre', 'correo', 'telefono']
    search_fields = ['nombre', 'correo', 'telefono']
    ordering_fields = ['id', 'nombre']

class EmpleadoViewset(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['nombre', 'telefono', 'cargo']
    search_fields = ['nombre', 'telefono', 'cargo']
    ordering_fields = ['id', 'nombre']

class FacturaVentaViewset(viewsets.ModelViewSet):
    queryset = FacturaVenta.objects.all()
    serializer_class = FacturaVentaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['fecha', 'id_cliente', 'id_empleado']
    search_fields = ['id_cliente__nombre', 'id_empleado__nombre']
    ordering_fields = ['id', 'fecha']

class DetalleVentaViewset(viewsets.ModelViewSet):
    queryset = DetalleVenta.objects.all()
    serializer_class = DetalleVentaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['cantidad', 'precio_unitario', 'id_factura', 'id_producto']
    search_fields = ['id_factura__id', 'id_producto__nombre']
    ordering_fields = ['id', 'cantidad', 'precio_unitario']

class MovimientoViewset(viewsets.ModelViewSet):
    queryset = Movimiento.objects.all()
    serializer_class = MovimientoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['tipo', 'fecha', 'id_producto', 'id_cliente']
    search_fields = ['tipo', 'id_producto__nombre', 'id_cliente__nombre']
    ordering_fields = ['id', 'fecha', 'cantidad']
