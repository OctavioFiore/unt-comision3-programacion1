
#Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.
def imprimir_hola():
    
    print("Hola mundo!")


imprimir_hola()

"""Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario."""



def saludar_usuario(nombre):
    
    return f"Hola {nombre}!"

nombre_usuario = input("Ingrese su nombre: ").capitalize().strip()
saludar = saludar_usuario(nombre_usuario)
print(saludar)

"""3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

"""
def pedir_entero(mensaje):

        while True:

                n = input(mensaje)

                if n.isdigit():

                        return int(n)
                else:
                        print("Error:ingrese un número entero")



def informacion_personal(nombre,apellido,edad,residencia):

    
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"



nombre = input("Ingrese su nombre: ").capitalize().strip()

apellido = input("Ingrese su apellido: ").capitalize().strip()

edad = pedir_entero("Ingrese su edad: ")

residencia = input("Ingrese su residencia: ").capitalize().strip()

informacion_per = informacion_personal(nombre,apellido,edad,residencia)
print(informacion_per)


"""
4.Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados
"""
import math

def pedir_float(mensaje):
    while True:
        n = input(mensaje)
        try:
            return float(n)
        except ValueError:
            print("Error: ingrese un número válido")

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = pedir_float("Ingrese el radio: ")
if radio <= 0:
    print("Error: el radio debe ser mayor que 0.")
else:
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f"El área del círculo es: {area:.2f}")
    print(f"El perímetro del círculo es: {perimetro:.2f}")

"""5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función."""

def segundos_a_horas(segundos):
        segundos = segundos / 3600


        return segundos

def pedir_entero(mensaje):

        while True:

                n = input(mensaje)

                if n.isdigit():

                        return int(n)
                else:
                        print("Error:ingrese un número entero")



segundo = pedir_entero("Ingrese segundos: ")

print(f"De segundos a hora es: {segundos_a_horas(segundo)}")


"""
6.Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función.
"""
def tabla_multiplicar(numero):
    for i in range(1,11):
        
        resultado = i * numero
        
        print(f"{numero} X {i} = {resultado}")
        
def pedir_entero(mensaje):

    while True:

        n = input(mensaje)

        if n.isdigit():

            return int(n)
        else:
            print("Error:ingrese un número entero")

n = pedir_entero("Ingrese un número: ")
print(tabla_multiplicar(n))

"""
7.Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado
de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara
"""
def operaciones_basicas(a,b):
    suma = a + b

    resta = a - b

    multiplicarlos = a * b

    div = a / b

    resultado_de_tupla = (suma,resta,multiplicarlos,div)

    return resultado_de_tupla



def pedir_entero(mensaje):

    while True:

        n = input(mensaje)

        if n.isdigit():

            return int(n)
        else:
            print("Error:ingrese un número entero")
            

    

numero = pedir_entero("Ingrese el primer número: ")

numero2 = pedir_entero("Ingrese el segundo número: ")

tupla = (operaciones_basicas(numero,numero2))
print(tupla)


"""
8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
ción para mostrar el resultado con dos decimales.     
"""

def calcular_impc(peso, altura):
    return peso / (altura ** 2)




def pedir_float(mensaje):

    while True:

        n = input(mensaje)

        try:
            return float(n)

        except ValueError:
            print("Error:Ingrese número valido")

peso = pedir_float("Ingrese el peso kilogramos: ")
altura = pedir_float("Ingrese la altura en metros: ")
imc = calcular_impc(peso,altura)

print(f"El imc es: {imc:.2f}")


"""9.Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.
"""

def celsius_a_fahrenheit(celcius):

    return (celcius * 1.8) + 32

def pedir_float(mensaje):

    while True:

        n = input(mensaje)

        try:
            return float(n)

        except ValueError:
            print("Error:Ingrese número valido")

celcius = pedir_float("Ingrese la temperatura en celsius: ")

fahrenheit = celsius_a_fahrenheit(celcius)
print(f"La temperatura en celsius su equivalente en fahrenheit es: {fahrenheit:.2f} ")

"""10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función."""

def calcular_promedio(a,b,c):
    return (a+b+c)/3



def pedir_float(mensaje):

    while True:

        n = input(mensaje)

        try:
            return float(n)

        except ValueError:
            print("Error:Ingrese número valido")

num = pedir_float("Ingrese un número: ")
num2 = pedir_float("Ingrese el segundo número: ")
num3 = pedir_float("Ingrese el tercer número: ")


promedio = calcular_promedio(num,num2,num3)

print(f"El promedio de {num},{num2},{num3} es: {promedio:.2f}")





