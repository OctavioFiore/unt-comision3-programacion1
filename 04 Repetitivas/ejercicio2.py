"""
2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene.
"""
numero = float(input("Ingrese unos numeros: "))

numero = abs(numero)

contador=0


if numero == 0:
    contador=1
else:
    while numero>0:
        numero//=10
        print(numero)
        contador+=1
    




print(f"El numero contiene {contador} cantidad de digitos")

