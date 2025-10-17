
"""
1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300
"""
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450
}

precios_frutas.update({"Naranja":1200,"Manzana" : 1500,"Pera" : 2300})

print(precios_frutas)
"""
2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800"""


precios_frutas["Banana"] = 1330

precios_frutas["Manzana"] = 1700

precios_frutas["Melón"] = 2800

print(precios_frutas)

"""
3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios."""
lista_de_frutos =['Banana', 'Ananá', 'Melón', 'Uva', 'Naranja', 'Manzana', 'Pera']

for i in range(len(lista_de_frutos)):
    print(f"{lista_de_frutos[i]}")

"""
4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe.
Ejemplo:

"""
def pedir_entero(mensaje):
    
    while True:

        try:
            num = int(input(mensaje))
            return num
        except ValueError:
            print("⚠ Error:Ingrese un valor entero")
        

contactos ={
}
for i in range(5):
    clave = input("Ingrese una clave: ").title().strip()

    valor = pedir_entero("Ingrese un valor: ")

    contactos[clave] = valor
    
    

print(contactos)

"""5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra.
Ejemplo:
"""



frase = input("Ingrese una frase: ").lower().strip()

palabras = frase.split()
palabra_unicos = set(palabras)
print(palabra_unicos)
contador={}

for palabra in palabras:

    if palabra in contador:
        contador[palabra]+=1
    else:
        contador[palabra]=1

print(f"Cantidad de veces que se repite una palabra es:{contador}")
"""6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno.
Ejemplo:"""
def pedir_entero(mensaje):
    
    while True:

        try:
            num = int(input(mensaje))
            return num
        except ValueError:
            print("⚠ Error:Ingrese un valor entero") 



alumnos = {}  

for i in range(3):
    alumno = input("Ingrese el nombre del alumno: ").title().strip()

    notas = []
    for j in range(3):  
        nota = pedir_entero(f"Ingrese la nota {j+1} de {alumno}: ")
        notas.append(nota)

    alumnos[alumno] = tuple(notas)  

print("-----Promedio de notas-----")

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}  (notas: {notas})")
    
    
"""7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)."""

alumnos_primer_parcial = {"Ana", "Luis", "Carla", "Mateo", "Sofía"}
alumnos_segundo_parcial = {"Luis", "Sofía", "Tomi", "Camila", "Mateo"}
    
aprobados_ambos = alumnos_primer_parcial & alumnos_segundo_parcial

solo_uno = alumnos_primer_parcial ^ alumnos_segundo_parcial

aprobado_alguno = alumnos_primer_parcial | alumnos_segundo_parcial


    

print(f"Las personas que aprobaron ambos parciales {aprobados_ambos}")

print(f"Las personas que aprobaron solo un parcial {solo_uno}")

print(f"Las personas aprobaron al menos un parcial{aprobado_alguno}")


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

            if not productos:
                print("⚠ No hay productos cargados aún.")
                continue

            prod = input("Ingrese el nombre del producto a consultar: ").title().strip()
            if prod in productos:
                print(f"{prod}: {productos[prod]} unidades en stock.")
            else:
                print(" El producto no existe en el inventario.")

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








"""9) Creá una agenda donde las claves sean tuplas (día, hora)
y los valores sean eventos. Permití consultar qué actividad hay
en cierto día y hora.
"""

agenda = {
    ("lunes", "10:00"): "Parcial de Programación",
    ("martes", "08:00"): "Clase de Organización",
    ("jueves", "12:10"): "Clases de consulta"
}



for consulta in (agenda):
    print(f"Consulta\n {consulta}")



dia = input("\nIngrese el día de la consulta: ").lower().strip()
hora = input("Ingrese la hora: ").strip()


if (dia, hora) in agenda:
    print(f"\n El día {dia} a las {hora}: {agenda[(dia, hora)]}")
else:
    print(f"\n No hay actividades el {dia} a las {hora}.")


"""10) Dado un diccionario país → capital,
crear uno nuevo capital → país
"""

paises = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción",
    "Brasil": "Brasilia"
}


capitales = {}

for pais, capital in paises.items():
    capitales[capital] = pais

print(f"Diccionario original : {paises}")

print(f"Diccionario invertido : {capitales}")

    
            



    


