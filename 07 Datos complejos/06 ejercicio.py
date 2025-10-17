"""[[6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno.
Ejemplo:]]"""
def pedir_entero(mensaje):
    
    while True:

        try:
            num = int(input(mensaje))
            return num
        except ValueError:
            print("⚠ Error:Ingrese un valor entero") 



alumnos = {}  

for i in range(3):
    alumno = input("Ingrese el nombre del alumno: ").title().strip()

    notas = []
    for j in range(3):  
        nota = pedir_entero(f"Ingrese la nota {j+1} de {alumno}: ")
        notas.append(nota)

    alumnos[alumno] = tuple(notas)  

print("-----Promedio de notas-----")

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}  (notas: {notas})")
    
    





