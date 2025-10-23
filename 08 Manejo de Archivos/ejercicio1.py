"""1. Crear archivo inicial con productos: Crear un archivo de texto llamado 
productos.txt con tres productos. Cada línea debe tener:  nombre,precio,cantidad

"""
def pedir_float(mensaje):
    while True:
        try:
            num = float(input(mensaje))
            return num
        except ValueError:
            print("⚠ Error: Ingrese un número válido")

def pedir_entero(mensaje):
    while True:
        try:
            num = int(input(mensaje))
            return num
        except ValueError:
            print("⚠ Error: Ingrese un número válido")

def pedir_nombre(mensaje):
    while True:
        nombre = input(mensaje).strip().lower()
        if not nombre:
            print("⚠ Ingrese un nombre no vacío.")
            continue
        if "," in nombre:
            print("⚠ No use comas (separa columnas).")
            continue
        return nombre

def crear_archivo():
    with open("productos.txt", "w", encoding="utf-8") as archivo:
        nombre = pedir_nombre("Ingrese el nombre del producto: ")
        precio = pedir_float("Ingrese un precio: ")
        cantidad = pedir_entero("Ingrese una cantidad: ")
        archivo.write(f"{nombre},{precio},{cantidad}\n")
    print("Archivo creado correctamente.")

def agregar_producto():
    with open("productos.txt", "a", encoding="utf-8") as archivo:
        nombre = pedir_nombre("Ingrese el nombre del producto: ")
        precio = pedir_float("Ingrese un precio: ")
        cantidad = pedir_entero("Ingrese una cantidad: ")
        archivo.write(f"{nombre},{precio},{cantidad}\n")
    print("Producto agregado con éxito.")

def mostrar_productos():
    try:
        with open("productos.txt", "r", encoding="utf-8") as archivo:
            print("\nProductos cargados:\n")
            for dato in archivo:
                nombre, precio_str, cant_str = dato.strip().split(",")
                precio = float(precio_str)
                cantidad = int(float(cant_str))
                print(f"{nombre.capitalize():<15} | ${precio:>7.2f} | {cantidad:>3} unidades")
    except FileNotFoundError:
        print("⚠ No existe el archivo 'productos.txt'.")

def cargar_productos_en_lista():
    productos = []
    try:
        with open("productos.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(",")
                prod = {
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(float(cantidad))
                }
                productos.append(prod)
        print("Productos cargados correctamente en la lista.")
        return productos
    except FileNotFoundError:
        print("⚠ No existe el archivo 'productos.txt'.")
        return []

def buscar_producto(lista):
    producto = pedir_nombre("Ingrese el producto a buscar: ")
    encontrado = False
    for p in lista:
        if p["nombre"] == producto:
            print(f"\nProducto encontrado:")
            print(f"{p['nombre'].capitalize()} | ${p['precio']:.2f} | {p['cantidad']} unidades")
            encontrado = True
            break
    if not encontrado:
        print(f"⚠ No se encontró el producto '{producto}'.")

def menu():
    print("\n" + "-" * 10, "MENU", "-" * 10)
    print("1_Crear archivo inicial")
    print("2_Mostrar productos")
    print("3_Agregar producto")
    print("4_Cargar productos en lista")
    print("5_Buscar producto por nombre")
    print("6_Salir")
    return pedir_entero("➡ Elija una opción: ")

def main():
    while True:
        opcion = menu()
        match opcion:
            case 1:
                crear_archivo()
            case 2:
                mostrar_productos()
            case 3:
                agregar_producto()
            case 4:
                cargar_productos_en_lista()
            case 5:
                lista = cargar_productos_en_lista()
                buscar_producto(lista)
            case 6:
                print("Saliendo...")
                break
            case _:
                print("⚠ Opción no válida.")

if __name__ == "__main__":
    main()

