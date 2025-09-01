
#1)Crea una variable llamada "numero1" y asígnale un número entero de tu elección. 
numero1 = 4
print(f'El valor entero es:{numero1}')
print("-------------------------------------")
#2)No borres la variable número uno y crea una variable llamada "numero2" asignándole 
#un número decimal de tu elección."""
numero2 = 2.4
print(f'El valor decimal es:{numero2}')
print("-------------------------------------")

#3)Crear una variable llamada "suma" y almacena la suma de "numero1" y "numero2"
suma = numero1 + numero2
resta = numero1 + numero2
multiplicacion = numero1 + numero2
division = numero1 / numero2
#4)Ahora crear tres variables más sin borrar lo que tienes. Una para resta, otra para 
#multiplicación y otra para división. Imprime estas variables. 
print(f'La suma:{suma}')
print("-------------------------------------")
print(f'La resta:{resta}')
print("-------------------------------------")
print(f'La multiplicacion:{multiplicacion}')
print("-------------------------------------")
print(f'La division:{division}')
print("-------------------------------------")
#5)Crea una variable llamada "nombre" y asígnale tu nombre como valor
nombre="Octavio"
print(f'Mi nombre es:{nombre}')
print("-------------------------------------")
#6)Crea una variable llamada "precio" y asígnale un valor decimal que represente el 
#precio de un artículo ficticio. 
precio=250.25
print(f'El valor de precio:{precio}')
print("-------------------------------------")
#7)Ahora, sin borrar la variable anterior, crea una variable llamada "descuento" y asígnale
# un valor decimal que represente el descuento aplicado al artículo. Por ejemplo, si le 
#quieres aplicar un 25% de descuento, dale un valor de 0,25. El valor 1 equivaldría al 
#100% y el valor 0 al 0%. 

descuento=0.40
print(f'El descuento es:{descuento}')
print("-------------------------------------")

#8)Ahora, intenta calcular el precio final aplicando el descuento al precio original y 
#almacena el resultado en una variable llamada "precio_final". Para ello vas a tener que 
#aplicar la lógica de matemáticas. 

descuento_final=precio*descuento
precio_final = precio-descuento_final
print(f'El precio final es:{precio_final}')
print("-------------------------------------")

#9)Crea una variable llamada "cadena" y asignale un texto, una frase, lo que quieras de tu 
#elección. Qué sea un string. 
cadena="Vamos Argentina"
print(f'La frase es {cadena}')
#10)Sin borrar la variable "cadena", crea una nueva variable llamada "longitud". En ella, vas 
#a almacenar la longitud en caracteres de la cadena utilizando una de las funciones de 
#Python. 

longitud=len(cadena)
print(f'La cantidad de letras de {cadena} es:{longitud}')
print("-------------------------------------")

#11)crea otra vez la variable llamada "precio" y dale un valor decimal, el que sea y 
#conviértelo en número entero. Lo puedes hacer en la misma variable o en otra, da lo 
#mismo. 
precio=10
#12)Crea dos variables. Una se va a llamar "nombre" y la segunda "apellido" concaténalas 
#en una tercera variable llamada "nombre_completo", el nombre y el apellido con un 
#espacio entre medio. Puedes usar libremente la forma de concatenación que quieras. 
nombre="Octavio"
apellido="Fiore"
nombre_completo=f'{nombre} {apellido} '
print(nombre_completo)
print("-------------------------------------")
#13)Escribe tu edad en una variable. Increméntala en 5 y luego disminúyela en 10
edad=20
edad_inc=20+5
edad_dis=20-10

print(f'Mi edad:{edad}')
print(f'Mi edad si le incremento 5: {edad_inc}')
print(f'Mi edad si le disminuyo 10:{edad_dis}')
print("-------------------------------------")

#14)Crea una variable llamada "altura" que contenga con decimales, tu altura en metros y 
#centímetros. Por ejemplo: 1.83.  Multiplícala por 4 y luego divídela en 3. 
altura=1.65
mult=altura*4
div=altura/3
print(f'Mi altura es:{altura}')
print(f'Mi altura se la multiplicas por 4:{mult}')
print(f'Mi altura si la divide en 3:{div}')
print("-------------------------------------")
#15)Crea una variable que contenga tu nombre completamente en mayúsculas. Después 
#transfórmalo todo en minúsculas con algún método o función de Python
nombre_mayuscula="OCTAVIO"
nombre_minuscula=nombre_mayuscula.lower()
print(f'Mi nombre en todo minuscula {nombre_minuscula}')
print("-------------------------------------")

#16 Por último, con la variable con el nombre en mayúsculas, aplica un método parecido 
#para que se transforme todo en minúsculas excepto la primera letra. 
primera_letra_mayuscula=nombre_mayuscula[0].upper()+ nombre_mayuscula[1:].lower()

print(f'solo siendo la primera en letra en mayuscula es {primera_letra_mayuscula}')











