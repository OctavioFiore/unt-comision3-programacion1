""". Generá un cartón 5x5 con números aleatorios entre 1 y 50, sin repetirse. 
2. Mostrá el cartón al jugador en forma de matriz. 
3. El programa debe sortear números al azar entre 1 y 50, uno por uno. 
4. Cada vez que salga un número: 
o Si está en el cartón, reemplazarlo por un 0. 
o Si no está, avisar que no aparece. 
o Mostrar el cartón actualizado después de cada sorteo. 
5. El juego termina cuando el cartón completo queda en 0 (¡Bingo!).
"""

import random


numeros = random.sample(range(1, 51), 25)
carton = [numeros[i:i+5] for i in range(0, 25, 5)]


print("Bienvenido al bingo")
print("-------------------------")

bolillero = list(range(1, 51))
for fila in carton:
    print(" ".join(f"{n:2d}" for n in fila))
print()


lineas_reportadas = [False] * 5


while True:
    opcion = input("¿Sacar una bolilla? (s/n): ").lower().strip()
    if opcion == "n":
        break
    if not bolillero:
        print("No quedan bolillas.")
        break


    numero = random.choice(bolillero)
    bolillero.remove(numero)
    print(f"Sale: {numero}")


    encontrado = False
    for i in range(5):
        for j in range(5):
            if carton[i][j] == numero:
                carton[i][j] = 0
                encontrado = True

    if not encontrado:
        print("No aparece en el cartón.")


    for fila in carton:
        print(" ".join(f"{n:2d}" for n in fila))
    print()

    
    for idx, fila in enumerate(carton):
        if not lineas_reportadas[idx] and all(n == 0 for n in fila):
            print(f"¡Línea en la fila {idx+1}!")
            lineas_reportadas[idx] = True


    if all(all(n == 0 for n in fila) for fila in carton):
        print("¡Bingo!")
        break

