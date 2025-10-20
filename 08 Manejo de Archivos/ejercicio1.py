"""1. Crear archivo inicial con productos: Crear un archivo de texto llamado 
productos.txt con tres productos. Cada línea debe tener:  nombre,precio,cantidad

"""
def pedir_float(mensaje):


    while True:
        
        try:
            num = float(input(mensaje))
            return num
        except ValueError:
            print("⚠ Error: Ingrese un número valido")
            


def pedir_entero(mensaje):

    
    while True:
        try:
            num = int(input(mensaje))
            return num
        
        except ValueError:
            print("⚠ Error: Ingrese un número valido")

def pedir_nombre(mensaje):
    while True:
        nombre = input(mensaje).strip().lower()
        if not nombre:
            print("⚠ Ingrese un nombre no vacío.")
            continue
        if "," in nombre:
            print("⚠ No use comas en el nombre (separa columnas).")
            continue
        return nombre
            


        


with open("productos.txt", "w", encoding="utf-8") as archivo:


    for i in range(3):
        nombre = pedir_nombre("Ingrese el nombre del producto: ")
        precio = pedir_float("Ingrese un precio: ")
        cantidad = pedir_entero("Ingrese una cantidad de linea: ")

        archivo.write(f"{nombre},{precio},{cantidad}\n")




with open("productos.txt","r",encoding="utf-8") as archivo:
    for dato in archivo:
        nombre, precio_str, cant_str = dato.strip().split(",")
        precio = float(precio_str)
        cantidad = int(float(cant_str))  
        print(f"{nombre} | {precio:.2f} | {cantidad} unidades")