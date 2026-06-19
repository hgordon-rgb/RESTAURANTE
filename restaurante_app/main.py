from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

# Crear restaurante
restaurante = Restaurante("Mi Restaurante")

# Crear productos
p1 = Producto("Hamburguesa", 5.5, "Comida")
p2 = Producto("Jugo Natural", 2.0, "Bebida")

# Crear clientes
c1 = Cliente("Juan Perez", "1234567890")
c2 = Cliente("Maria Lopez", "0987654321")

# Agregar al sistema
restaurante.agregar_producto(p1)
restaurante.agregar_producto(p2)

restaurante.agregar_cliente(c1)
restaurante.agregar_cliente(c2)

# Mostrar información
print(f"Sistema del {restaurante.nombre}")
restaurante.mostrar_productos()
restaurante.mostrar_clientes()