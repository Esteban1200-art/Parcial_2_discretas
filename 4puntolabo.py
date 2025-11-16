class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    # Aumentar stock (compra)
    def aumentar_stock(self, unidades):
        if unidades > 0:
            self.cantidad += unidades
            print(f"Stock aumentado. Nuevo stock de {self.nombre}: {self.cantidad}")
        else:
            print("Error: la cantidad debe ser positiva.")

    # Disminuir stock (venta)
    def disminuir_stock(self, unidades):
        if unidades <= 0:
            print("Error: la cantidad debe ser positiva.")
        elif unidades > self.cantidad:
            print(f"No hay suficiente stock de {self.nombre}.")
        else:
            self.cantidad -= unidades
            print(f"Venta realizada. Nuevo stock de {self.nombre}: {self.cantidad}")

def mostrar_inventario(lista_productos):
    print("\n=== INVENTARIO ACTUAL ===")
    for producto in lista_productos:
        print(f"Producto: {producto.nombre} | Precio: ${producto.precio} | Stock: {producto.cantidad}")
    print("==========================\n")


inventario = []

print("=== SISTEMA DE INVENTARIO ===")
num_productos = int(input("¿Cuántos productos desea ingresar? "))

for i in range(num_productos):
    print(f"\nProducto #{i+1}")

    nombre = input("Nombre del producto: ")

    precio = float(input("Precio del producto: "))

    cantidad = int(input("Cantidad inicial en stock: "))

    # Crear instancia de producto
    producto = Producto(nombre, precio, cantidad)
    inventario.append(producto)

# Mostrar inventario inicial
mostrar_inventario(inventario)

print("=== SIMULACIÓN DE MOVIMIENTOS ===")

for producto in inventario:
    print(f"\n--- Producto: {producto.nombre} ---")

    compra = int(input(f"¿Cuántas unidades desea COMPRAR de {producto.nombre}? "))
    producto.aumentar_stock(compra)

    venta = int(input(f"¿Cuántas unidades desea VENDER de {producto.nombre}? "))
    producto.disminuir_stock(venta)

# Mostrar inventario final
mostrar_inventario(inventario)
print("Fin del sistema de inventario.")