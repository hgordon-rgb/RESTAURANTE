class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria  # Ej: comida, bebida

    def __str__(self):
        return f"{self.nombre} - ${self.precio} ({self.categoria})"