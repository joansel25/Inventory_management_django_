from locust import HttpUser, task, between
import json
import random

class FarmaciaUser(HttpUser):
    wait_time = between(1, 3)  # espera entre requests para simular usuarios reales

    def on_start(self):
        """
        Se ejecuta cuando un usuario virtual empieza.
        Obtiene token JWT para autenticación.
        """
        self.username = "andres"
        self.password = "andres123"

        response = self.client.post(
            "/farmacia/api/token/",
            data={"username": self.username, "password": self.password}
        )

        if response.status_code == 200:
            self.token = response.json()["access"]
            self.headers = {"Authorization": f"Bearer {self.token}"}
            print("Token JWT obtenido correctamente")
        else:
            print(f"Error obteniendo token JWT: {response.text}")
            self.token = None
            self.headers = {}

    # -------------------- CLIENTES --------------------
    @task(2)
    def listar_clientes(self):
        if self.token:
            self.client.get("/farmacia/api/clientes/", headers=self.headers)

    @task(1)
    def crear_cliente(self):
        if self.token:
            data = {
                "nombre": f"Cliente {random.randint(1,1000)}",
                "correo": f"cliente{random.randint(1,1000)}@example.com",
                "telefono": f"300{random.randint(1000000,9999999)}"
            }
            self.client.post("/farmacia/api/clientes/", headers=self.headers, json=data)

    # -------------------- PRODUCTOS --------------------
    @task(2)
    def listar_productos(self):
        if self.token:
            self.client.get("/farmacia/api/productos/", headers=self.headers)

    @task(1)
    def crear_producto(self):
        if self.token:
            data = {
                "nombre": f"Producto {random.randint(1,1000)}",
                "precio": random.randint(1000, 50000),
                "categoria": 1,  # asegúrate que exista la categoria 1
                "stock": random.randint(1, 50)
            }
            self.client.post("/farmacia/api/productos/", headers=self.headers, json=data)

    @task(1)
    def actualizar_producto(self):
        if self.token:
            response = self.client.get("/farmacia/api/productos/", headers=self.headers)
            productos = response.json()
            if productos:
                product_id = productos[0]["id"]
                self.client.patch(
                    f"/farmacia/api/productos/{product_id}/",
                    headers=self.headers,
                    json={"precio": random.randint(2000, 60000)}
                )

    @task(1)
    def eliminar_producto(self):
        if self.token:
            response = self.client.get("/farmacia/api/productos/", headers=self.headers)
            productos = response.json()
            if productos:
                product_id = productos[-1]["id"]
                self.client.delete(f"/farmacia/api/productos/{product_id}/", headers=self.headers)

    # -------------------- PROVEEDORES --------------------
    @task(1)
    def listar_proveedores(self):
        if self.token:
            self.client.get("/farmacia/api/proveedores/", headers=self.headers)

    @task(1)
    def crear_proveedor(self):
        if self.token:
            data = {
                "nombre": f"Proveedor {random.randint(1,1000)}",
                "correo": f"proveedor{random.randint(1,1000)}@example.com",
                "telefono": f"300{random.randint(1000000,9999999)}"
            }
            self.client.post("/farmacia/api/proveedores/", headers=self.headers, json=data)

    # -------------------- CATEGORIAS --------------------
    @task(1)
    def listar_categorias(self):
        if self.token:
            self.client.get("/farmacia/api/categorias/", headers=self.headers)

    # -------------------- FACTURAS --------------------
    @task(1)
    def crear_factura(self):
        if self.token:
            # Primero obtener un cliente y productos existentes
            clientes = self.client.get("/farmacia/api/clientes/", headers=self.headers).json()
            productos = self.client.get("/farmacia/api/productos/", headers=self.headers).json()
            if clientes and productos:
                cliente_id = clientes[0]["id"]
                producto_id = productos[0]["id"]
                data = {
                    "cliente": cliente_id,
                    "total": productos[0]["precio"],
                    "detalles": [
                        {"producto": producto_id, "cantidad": 1, "precio": productos[0]["precio"]}
                    ]
                }
                self.client.post("/farmacia/api/facturas/", headers=self.headers, json=data)
