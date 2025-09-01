"""Un grupo de amigos decide organizar un juego de estrategia, para lo cual forman 
dos equipos de 6 integrantes cada uno, donde un integrante de cada equipo es el 
“jefe” y los otros 5 son sus “oficiales”. La regla más importante del juego es que 
sólo se comunicarán mediante un canal común, por lo que deben buscar la forma 
de ocultar el contenido de sus mensajes. Uno de los equipos decide utilizar un 
método antiguo de encriptación llamado “la cifra del césar”, que consiste en 
correr cada letra del mensaje –considerando la posición de cada una en el 
alfabeto– una determinada cantidad de lugares. Ejemplo: si el corrimiento es de 2 
lugares, la palabra “ATAQUE” se transforma en “CVCSWG”. Cada día, el “jefe” del 
equipo debe enviar un mensaje a cada uno de sus oficiales.  
Escribir un programa que permita encriptar los 5 mensajes. El corrimiento 
(cantidad de lugares que se correrán las letras) será dado por el usuario antes de 
comenzar a encriptar. Los 5 mensajes usarán el mismo corrimiento. Nota: si el 
alfabeto termina antes de poder correr la cantidad de lugares necesarios, se 
vuelve a comenzar desde la letra “a”.  
Ejemplo: la palabra “EXTRA” corrida 3 lugares se convierte en “HAWUD”. 
Utilizando el alfabeto español, de 27 letras, el siguiente cálculo matemático 
permite volver a comenzar por el principio una vez que se llegó a la “z”: (índice de 
la letra a correr+corrimiento)%27 Sólo se encriptarán las letras de los mensajes, 
dejando al resto de caracteres sin modificación."""

"""""
ALFABETO_MINUSCULA = "abcdefghijklmnñopqrstuvwxyz"
for i in range(5):
        # El mensaje se pide DENTRO del bucle para que sea un mensaje nuevo cada vez
        mensaje_original = input(f"Ingrese el mensaje {i+1}: ").lower()
        
        # Inicializamos la variable que guardará el mensaje encriptado
        mensaje_cifrado = ""
        
        # Bucle interno: recorre CADA caracter del mensaje
        for letra in mensaje_original:
            # Comprobamos si el caracter es una letra del alfabeto
            if letra in alfabeto:
                nueva_pos = (alfabeto.index(letra) + corrimiento) % 27
                # AGREGAMOS la nueva letra encriptada al mensaje final
                mensaje_cifrado += alfabeto[nueva_pos]
            else:
                # Si NO es una letra (espacio, número, etc.), la agregamos sin encriptar
                mensaje_cifrado += letra
        
        # Imprimimos el resultado de la encriptación
        print(f"Mensaje encriptado: {mensaje_cifrado}\n")


"""""








"""
Vas a programar un juego clásico contra la computadora: Piedra, papel o tijeras. 
Reglas: 
1. El programa debe mostrar un menú con las opciones: 
o Piedra 
o Papel 
o Tijera 
2. El jugador elegirá una opción. 
3. La computadora elegirá su jugada al azar. 
4. El programa debe comparar ambas jugadas y mostrar quién gana: 
o Piedra vence a Tijera. 
o Tijera vence a Papel. 
o Papel vence a Piedra. 
o Si ambos eligen lo mismo, es empate. 
Extra (para hacerlo más divertido): 
• Llevar un marcador de cuántas partidas gana el jugador y cuántas gana la 
computadora. 
• El juego termina cuando el jugador elija salir, mostrando el resultado final.
"""


opcion = 1
jugador_puntos=0
npc_puntos=0


while opcion != 0 :

    
    import random

    mano_jugador = input("o Piedra\no Papel\no Tijera\n Opcion: ") .lower()
    jugada = ["piedra","papel","tijera"]
    npc = random.choice(jugada)
    print("------------------------")
    if mano_jugador == npc:
        print("Empate 0 puntos para los dos")
    elif (mano_jugador == "papel"and npc=="piedra") or (mano_jugador == "piedra"and npc == "papel"):
        if mano_jugador == "papel":
            jugador_puntos += 1
        else:
            npc_puntos += 1
    elif (mano_jugador == "tijera"and npc == "papel") or (mano_jugador == "papel" and npc == "tijera"):
        if mano_jugador == "tijera":
            jugador_puntos+=1
        else:
            npc_puntos=+1
    elif (mano_jugador == "piedra"and npc=="tijera")or(mano_jugador == "tijera"and npc == "piedra"):
        if mano_jugador == "tijera":
            jugador_puntos+=1
        else:
            npc_puntos+=1

    
    opcion = int(input("MENU DE OPCIONES:\n 1_Seguir jugando \n0_salir"))
print(f'PUNTOS FINALES:\nJUGADOR:{jugador_puntos}\nNPC:{npc_puntos}')

if jugador_puntos > npc_puntos:
    print("¡Felicidades, ganaste el juego! 🥳")
elif jugador_puntos < npc_puntos:
    print("El NPC ganó. ¡Suerte la próxima vez! 😔")
else:
    print("¡El juego terminó en un empate! 🤝")











"""
for letra in mensaje.lower():
        if letra in alfabeto:
            nueva_pos = (alfabeto.index(letra) + corrimiento) % 27
            resultado += alfabeto[nueva_pos]
        else:
            resultado += letra
    return resultado
    """