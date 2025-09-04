"""
8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio).
"""
numero = 0
positivo = 0
negativo = 0
par = 0
impar = 0
contador = 0
cantidad=int(input("Ingrese la cantidad de numeros: "))
while contador<cantidad:
    numero = int(input("Ingrese un numero entero: "))
    if numero > 0:
        positivo += 1
    else:
        negativo -= 1
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1
    contador+=1

print(f'La cantidad de números pares es: {par}\nLa cantidad de números impares es: {impar}\nLa cantidad de números positivos es: {positivo}\nLa cantidad de números negativos es: {negativo}')
