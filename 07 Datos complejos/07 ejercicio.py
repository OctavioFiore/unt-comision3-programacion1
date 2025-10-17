"""7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)."""

alumnos_primer_parcial = {"Ana", "Luis", "Carla", "Mateo", "Sofía"}
alumnos_segundo_parcial = {"Luis", "Sofía", "Tomi", "Camila", "Mateo"}
    
aprobados_ambos = alumnos_primer_parcial & alumnos_segundo_parcial

solo_uno = alumnos_primer_parcial ^ alumnos_segundo_parcial

aprobado_alguno = alumnos_primer_parcial | alumnos_segundo_parcial


    

print(f"Las personas que aprobaron ambos parciales {aprobados_ambos}")

print(f"Las personas que aprobaron solo un parcial {solo_uno}")

print(f"Las personas aprobaron al menos un parcial{aprobado_alguno}")









