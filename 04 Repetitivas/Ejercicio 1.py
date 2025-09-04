"""
1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
"""
for i in range(0,101):
    print(i)

"""
2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene.
"""
numero = int(input("Ingrese unos numeros: "))

numero = abs(numero)

contador = 0


if numero == 0:
    contador = 1
else:
    while numero > 0:
        numero //= 10
        contador += 1
    




print(f"El numero contiene {contador} cantidad de digitos")

"""3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores.
"""

numero = int(input("Ingrese el primer numero: "))

numero2 = int(input("Ingrese el segundo numero: "))

suma=0



menor=min(numero,numero2)
mayor=max(numero,numero2)


for i in range(menor+1,mayor):  
    suma += i

print(f'La suma de los enteros entre {numero} y {numero2} es: {suma}')


"""    
4)Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0.
"""


suma=0
acumulado=0
while True:
    
    opcion = int(input("Ingrese 0 si quiere salir: "))
    if opcion==0:
        break
    
    numero = int(input("Ingrese un numero: "))
    suma += numero
    

print(f'El total acumalado de la suma es: {suma}')

"""
5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
"""
import random

print("----- Adivina el número aleatorio entre 0 y 9 -----")

numero_aleatorio = random.randint(0, 9)
intentos = 0

while True:
    numero = int(input("Ingrese su número: "))
    intentos += 1

    if numero == numero_aleatorio:
        print(f"¡Acertaste! El número era {numero_aleatorio}")
        break
    else:
        print("No intenta de nuevo")

print(f"Intentos necesarios: {intentos}")

"""6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente
"""



for i in range(100,0,-1):
    if i%2==0:
        print(i)


"""
7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.
"""


while True:
    numero=int(input("Ingrese un numero entero(positivo): "))
    if numero>0:
        break
    else:
        print("Error: ingresó un número negativo. Intente de nuevo.")
        



suma=0
for i in range(0,numero+1):
    suma+=i



print(f'La suma de todos los números comprendidos entre 0 y {numero} es: {suma}')


"""
8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio).
"""



positivo = 0
negativo = 0
par = 0
impar = 0

cantidad = int(input("Ingrese la cantidad de números: "))

for i in range(cantidad):
    numero = int(input("Ingrese un número entero: "))
    
    if numero > 0:
        positivo += 1
    elif numero < 0:
        negativo += 1
    
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1

print(f'La cantidad de números pares es: {par}\nLa cantidad de números impares es: {impar}\nLa cantidad de números positivos es: {positivo}\nLa cantidad de números negativos es: {negativo}')


"""
9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).
"""

contador = 0
suma = 0
cantidad = int(input("Ingrese la cantidad de números: "))

while contador < cantidad:
    numero = int(input("Ingrese un número entero: "))

    suma += numero
    
    contador += 1

media = suma/cantidad
print(f'La media de estos valores: {media}')


"""
10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745"""

numero = int(input("Ingrese un número: "))

invertido = 0
while numero > 0:
    digito = numero % 10            
    invertido = invertido * 10 + digito
    numero //= 10                  

print(f"El número invertido es: {invertido}")

#askdkomasd




