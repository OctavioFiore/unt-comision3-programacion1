#1)Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("“Hola Mundo!”.")

#Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla
nombre=input("Ingrese un nombre ")
print(f"hola {nombre}!")


#2)Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

nombre=input("Ingrese un nombre ")
apellido=input("Ingrese un apellido ")
edad=int(input("Ingrese su edad "))
lugar=input("Ingrese lugar de residencia ")
print(f'Soy {nombre} {apellido}, tengo {edad} y vivo en {lugar}')

#3)Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.
import math
valor_de_pi=math.pi
radio=int(input("Ingrese el radio "))

area = valor_de_pi * (radio**2)
perimetro = 2 * valor_de_pi * radio

print(f"El area de un radio es: {area} y su perimetro es:{perimetro} ")
#4) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
#cuántas horas equivale.

segundos=int(input("Ingrese una cantidad de segundos "))

horas = segundos / 3600

print(f"La cantidad de horas equivalentes a segundo es: {horas}")

# Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
#multiplicar de dicho número.
numero=int(input("Ingrese un numero "))
resultado=0
print(f"{numero} x 1 = {numero*1}")
print(f"{numero} x 2 = {numero*2}")
print(f"{numero} x 3 = {numero*3}")
print(f"{numero} x 4 = {numero*4}")
print(f"{numero} x 5 = {numero*5}")
print(f"{numero} x 6 = {numero*6}")
print(f"{numero} x 7 = {numero*7}")
print(f"{numero} x 8 = {numero*8}")
print(f"{numero} x 9 = {numero*9}")
print(f"{numero} x 10 = {numero*10}")

# Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.


numero=int(input("Ingrese el primer numero (distinto al cero) "))

numero2=int(input("Ingrese el segundo numero (distinto al cero) "))

suma = numero + numero2

dividirlos = numero / numero2

multiplicarlos = numero * numero2

restarlos = numero - numero2

print(f"La suma:{numero}+{numero2}={suma}")
print("--------------------------")
print(f"La division:{numero}/{numero2}={dividirlos}")
print("--------------------------")
print(f"la multiplicacion:{numero}x{numero2}={multiplicarlos}")
print("--------------------------")
print(f"La resta:{numero}-{numero2}={restarlos}")


# Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
#de masa corporal.
peso=int(input("Ingrese el peso(peso en kilogramos) "))

altura=int(input("Ingrese la altura(altura metros)" ))

masa_corporal = peso / (altura**2)

print(f"Su indice de masa corporal es:{masa_corporal}")

#Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
#pantalla su equivalente en grados Fahrenheit
temperatura_en_celsius=int(input("Ingrese la temperatura en grados celsius"))

temperatura_en_fahrenheit = 9 / 5 * temperatura_en_celsius + 32

print(f"Su equivalente en grados Fahrenheit es:{temperatura_en_fahrenheit}")

#Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
#dichos números.
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))
suma_total = num1 + num2 + num3
promedio = suma_total / 3
print(f"El promedio de dichos numeros es:{promedio}")


