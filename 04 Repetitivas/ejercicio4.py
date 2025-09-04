"""    
4)Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0.
"""

opcion = 1
suma=0
acumulado=0
while 0!= opcion:
    
    opcion = int(input("Ingrese 0 si quiere salir: "))
    if opcion==0:
        break

    numero = int(input("Ingrese un numero: "))
    
    numero2 = int(input("Ingrese segundo numero: "))

    suma = numero + numero2

    acumulado+=suma

print(f"El total acumalado de la suma es: {acumulado}")



