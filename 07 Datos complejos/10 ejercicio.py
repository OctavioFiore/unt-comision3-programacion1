"""10) Dado un diccionario país → capital,
crear uno nuevo capital → país
"""

paises = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción",
    "Brasil": "Brasilia"
}


capitales = {}

for pais, capital in paises.items():
    capitales[capital] = pais

print(f"Diccionario original : {paises}")

print(f"Diccionario invertido : {capitales}")
