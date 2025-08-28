fecha=input("ingrese la fecha actual en formato “día,DD/MM”: " )
dia_semana,fecha_en_numeros=fecha.split(",")

dia,mes=fecha_en_numeros.split("/")
dia=int(dia)
mes=int(mes)

dia_semana=dia_semana.lower()

if dia>31 or mes>12:
    print("Error la fecha es incorrecta")
    exit()

if dia_semana=="lunes":
    print("Se dicta nivel inicial")
elif dia_semana=="martes":
    print("Se dicta clase nivel intermedio")
elif dia_semana =="miercoles":
    print("Se dicta clase nivel avanzado") 
elif dia_semana=="jueves ":
    print("Se dicta clase para práctica hablada ")
elif dia_semana=="viernes":
    print("Se dicta inglés para viajero") 
else:
    print("Es fin de semana y no se dicta clase")
    exit()



if dia_semana == "lunes" or dia_semana == "martes" or dia_semana == "miercoles":

    examen=input("Hubo examen(si o no)")
    examen=examen.lower()
    if examen == "si":    
        aprobados=int(input("Ingrese la cantidad de alumnos aprobados: "))
        desaprobados=int(input("Ingrese la cantidad de alumnos desaprobados: "))
        total=aprobados+desaprobados
        porcentaje=(aprobados/total)*100
        print(f'Porcentajes de aprobados es: {porcentaje}')
    elif examen == "no":
        print("No hubo examen")
    else:
        print("Es si o no hubo examen")


if dia_semana == "jueves":
    asistencia=input("Ingrese el porcentaje de asistencia a clase: ")
    if asistencia >=50:
        print("asistió la mayoría")
    else:
        print("no asistió la mayoría")




    

if dia == 1 and (mes==1 or mes==7):
    print("Comienzo de nuevo ciclo")
    cantidad_alumnos=int(input("Ingrese la cantidad de alumnos: "))
    cantidad_arancel=int(input("Ingrese la cantidad de arancel: "))
    total_en_plata=cantidad_arancel*cantidad_alumnos                   


