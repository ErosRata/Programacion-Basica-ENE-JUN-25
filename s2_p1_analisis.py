import csv
import re
from collections import Counter
import statistics

def validar_nombre(nombre):
    return re.match(r"^[a-zA-Z0-9\s\-]{2,50}$", nombre)

nombres = []
categorias = []

with open("medicamentos.csv", mode="r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        if validar_nombre(fila["Nombre"]):
            nombres.append(fila["Nombre"])
            categorias.append(fila["Categoría"])

conteo = Counter(categorias)
mediana = statistics.median([len(n) for n in nombres])
moda = statistics.mode(categorias)
print("Categorías más comunes:", conteo)
print("Longitud mediana de nombres:", mediana)
print("Categoría más frecuente:", moda)