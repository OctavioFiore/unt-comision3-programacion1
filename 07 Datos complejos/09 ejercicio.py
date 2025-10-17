



"""9) Creá una agenda donde las claves sean tuplas (día, hora)
y los valores sean eventos. Permití consultar qué actividad hay
en cierto día y hora.
"""

agenda = {
    ("lunes", "10:00"): "Parcial de Programación",
    ("martes", "08:00"): "Clase de Organización",
    ("jueves", "12:10"): "Clases de consulta"
}



for consulta in (agenda):
    print(f"Consulta\n {consulta}")



dia = input("\nIngrese el día de la consulta: ").lower().strip()
hora = input("Ingrese la hora: ").strip()


if (dia, hora) in agenda:
    print(f"\n El día {dia} a las {hora}: {agenda[(dia, hora)]}")
else:
    print(f"\n No hay actividades el {dia} a las {hora}.")