from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    nombre = models.CharField(max_length=150)
    contacto = models.CharField(max_length=100, unique=True)  # Si es email, cambiar a EmailField

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="productos")
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name="productos")

    def __str__(self):
        return f"{self.nombre} ({self.categoria.nombre})"


class Cliente(models.Model):
    nombre = models.CharField(max_length=150)
    correo = models.EmailField(unique=True)  # Si el correo debe ser único
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Empleado(models.Model):
    nombre = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20)
    cargo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class FacturaVenta(models.Model):
    fecha = models.DateField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="facturas")
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name="facturas")
    numero = models.CharField(max_length=20, unique=True, blank=True, null=True)  # Opcional: número de factura personalizado
    estado = models.CharField(max_length=20, default='pendiente')  # Ejemplo: pendiente, pagada, anulada

    def __str__(self):
        return f"Factura {self.numero or self.id}"


class DetalleVenta(models.Model):
    factura = models.ForeignKey(FacturaVenta, on_delete=models.CASCADE, related_name="detalles")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="detalles")
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle {self.id} (Factura {self.factura.id})"

    @property #Metodo subtotal para calcular y facilitar la
    def subtotal(self):
        return self.cantidad * self.precio_unitario


class Movimiento(models.Model):
    TIPOS_MOVIMIENTO = [
        ('entrada', 'Entrada'),
        ('salida', 'Salida'),
    ]

    tipo = models.CharField(max_length=10, choices=TIPOS_MOVIMIENTO)
    cantidad = models.PositiveIntegerField(default=1)
    fecha = models.DateTimeField(auto_now_add=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="movimientos")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="movimientos", blank=True, null=True)
    referencia = models.CharField(max_length=100, blank=True, null=True)  # Para anotar referencia o motivo del movimiento

    def __str__(self):
        return f"Movimiento {self.id} ({self.tipo})"
