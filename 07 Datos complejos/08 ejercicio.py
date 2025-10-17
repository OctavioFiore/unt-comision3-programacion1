"""8) Diccionario de productos y stock.
Permitir al usuario:
- Consultar el stock de un producto.
- Agregar unidades si ya existe.
- Agregar un nuevo producto si no existe.
"""

def pedir_entero(mensaje):
    while True:
        try:
            num = int(input(mensaje))
            return num
        except ValueError:
            print("⚠ Error: Ingrese un valor entero.")



cant = pedir_entero("Ingrese la cantidad de productos que desea cargar: ")

productos = {}

for i in range(cant):
    nombre = input(f"Ingrese el nombre del producto {i+1}: ").title().strip()
    stock = pedir_entero(f"Ingrese el stock de {nombre}: ")
    productos[nombre] = stock

print("Productos cargados correctamente.")


while True:
    print("Menú")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades a un producto existente")
    print("3. Agregar un nuevo producto si no existe")
    print("0. Salir")

    opcion = pedir_entero("Seleccione una opción: ")

    match opcion:
        case 1:
            # Consultar stock
            if not productos:
                print("⚠ No hay productos cargados aún.")
                continue

            prod = input("Ingrese el nombre del producto a consultar: ").title().strip()
            if prod in productos:
                print(f"📦 {prod}: {productos[prod]} unidades en stock.")
            else:
                print("❌ El producto no existe en el inventario.")

        case 2:
    
            if not productos:
                print("⚠ No hay productos cargados aún.")
                continue

            prod = input("Ingrese el nombre del producto: ").title().strip()
            if prod in productos:
                agregar = pedir_entero("¿Cuántas unidades desea agregar?: ")
                productos[prod] += agregar
                print(f"Nuevo stock de {prod}: {productos[prod]} unidades.")
            else:
                print("El producto no existe. Use la opción 3 para crearlo.")

        case 3:
            
            prod = input("Ingrese el nombre del nuevo producto: ").title().strip()
            if prod in productos:
                print("⚠ El producto ya existe.")
            else:
                stock = pedir_entero("Ingrese el stock inicial: ")
                productos[prod] = stock
                print(f"Producto agregado: {prod} ({stock} unidades)")

        case 0:
            print("Saliendo..")
            break

        case _:
            print("⚠ Opción inválida. Intente nuevamente.")


            









