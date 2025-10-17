"""
4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe.
Ejemplo:

"""
def pedir_entero(mensaje):
    
    while True:

        try:
            num = int(input(mensaje))
            return num
        except ValueError:
            print("⚠ Error:Ingrese un valor entero")
        

contactos ={
}
for i in range(5):
    clave = input("Ingrese una clave: ").title().strip()

    valor = pedir_entero("Ingrese un valor: ")

    contactos[clave] = valor
    
    

print(contactos)

