from rest_framework import serializers
from .models import (
    Categorias,Productos,Proveedores,
    Clientes,Empleados,FacturaVentas,
    DetalleVentas,Movimientos
)

# ModelSerializer: es una clase de DRF que automatiza la creación de serializadores basados en modelos de Django.
# Meta es una subclase que centralizar la configuración y metadatos del serializador
# fields: define qué campos del modelo se incluyen en la serialización 

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Proveedores
        fields= '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleados
        fields = '__all__'

class FacturaVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacturaVentas
        fields = '__all__'

class DetalleVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleVentas
        fields = '__all__'

class MovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimientos
        fields = '__all__'