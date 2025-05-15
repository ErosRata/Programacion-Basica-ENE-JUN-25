import csv
import matplotlib.pyplot as plt
from collections import Counter
from openpyxl import Workbook
import sys

nombres = []
categorias = []

with open("medicamentos.csv", mode="r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        nombres.append(fila["Nombre"])
        categorias.append(fila["Categoría"])

conteo = Counter(categorias)

wb = Workbook()
ws = wb.active
ws.append(["Categoría", "Cantidad"])

for cat, cant in conteo.items():
    ws.append([cat, cant])

nombre_archivo = sys.argv[1] if len(sys.argv) > 1 else "analisis_medicamentos.xlsx"
wb.save(nombre_archivo)
print(f"Excel guardado como {nombre_archivo}")

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.bar(conteo.keys(), conteo.values(), color="skyblue")
plt.xticks(rotation=45)
plt.title("Categorías de Medicamentos")

plt.subplot(2, 2, 2)
plt.pie(conteo.values(), labels=conteo.keys(), autopct='%1.1f%%')
plt.title("Distribución Porcentual")

plt.subplot(2, 2, 3)
plt.hist([len(n) for n in nombres], bins=5, color="orange")
plt.title("Histograma de Longitud de Nombres")

plt.subplot(2, 2, 4)
plt.scatter(range(len(nombres)), [len(c) for c in categorias], color="green")
plt.title("Dispersión nombre-categoría")

plt.tight_layout()
plt.savefig("graficas_medicamentos.png")
plt.show()