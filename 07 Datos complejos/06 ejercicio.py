"""[[6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno.
Ejemplo:]]"""
def pedir_entero(mensaje):
    
    while True:

        try:
            num = int(input(mensaje))
            return num
        except:
            print("⚠ Error:Ingrese un valor entero")   

for i in range(3):
    alumno = input("Ingrese el nombre de los alumnos: ").title().strip()
    


