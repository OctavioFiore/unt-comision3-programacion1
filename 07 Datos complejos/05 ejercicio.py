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
