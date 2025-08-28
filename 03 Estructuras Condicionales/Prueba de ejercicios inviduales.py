"""10)Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
si el usuario se encuentra en otoño, invierno, primavera o verano."""

hemisferio=input("Ingrese en cual hemisferio se encuentra (N/S)").lower()

mes=input("Ingrese que mes del año es: (ej: 'marzo') ").lower()
dia=int(input("Ingrese que dia del año es: (ej: '15')"))


if hemisferio=="n":
    if (dia>=21 and mes=="diciembre")or mes=="enero" or mes=="febrero" or ("marzo"==mes and dia<=20):
            print("Se encuentra en 'Invierno'")
    elif (dia>=21 and mes=="marzo")or mes=="abril" or mes=="mayo" or ("junio"==mes and dia<=20):
            print("Se encuentra en 'Primavera'")
    elif (dia>=21 and mes=="junio")or mes=="julio" or mes=="agosto" or ("septiembre"==mes and dia<=20):
            print("Se encuentra en 'Verano'")
    elif(dia>=21 and mes=="septiembre")or mes=="octubre" or mes=="noviembre" or ("diciembre"==mes and dia<=20):
            print("Se encuentra en 'Otoño'")
elif hemisferio=="s":    
    if (dia>=21 and mes=="diciembre")or mes=="enero" or mes=="febrero" or ("marzo"==mes and dia<=20):
            print("Se encuentra en 'verano'")
    elif (dia>=21 and mes=="marzo")or mes=="abril" or mes=="mayo" or ("junio"==mes and dia<=20):
            print("Se encuentra en 'Otoño'")
    elif (dia>=21 and mes=="junio")or mes=="julio" or mes=="agosto" or ("septiembre"==mes and dia<=20):
            print("Se encuentra en 'Invierno'")
    elif (dia>=21 and mes=="septiembre")or mes=="octubre" or mes=="noviembre" or ("diciembre"==mes and dia<=20):
            print("Se encuentra en 'Primavera'")
