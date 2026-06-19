from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        self.clientes = []

    # Agregar producto
    def agregar_producto(self, producto):
        self.productos.append(producto)

    # Agregar cliente
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    # Mostrar productos
    def mostrar_productos(self):
        print("\n--- Lista de Productos ---")
        for p in self.productos:
            print(p)

    # Mostrar clientes
    def mostrar_clientes(self):
        print("\n--- Lista de Clientes ---")
        for c in self.clientes:
            print(c)