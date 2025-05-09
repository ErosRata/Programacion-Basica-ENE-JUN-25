import csv
import sys
import matplotlib.pyplot as plt
import statistics
from openpyxl import Workbook
import re

def validar_nombre_archivo(nombre):
    patron = r'^[\w\-]+$'
    return re.match(patron, nombre) is not None

def cargar_datos(nombre_archivo):
    medicamentos = []
    try:
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                medicamentos.append(fila)
        return medicamentos
    except FileNotFoundError:
        print("Archivo no encontrado")
        sys.exit(1)

def analizar_medicamentos(medicamentos):
    descripciones = [len(m['description']) for m in medicamentos if m['description']]
    analisis = {
        'total_medicamentos': len(medicamentos),
        'promedio_longitud_descripcion': round(statistics.mean(descripciones), 2) if descripciones else 0,
        'descripcion_maxima': max(descripciones) if descripciones else 0,
        'descripcion_minima': min(descripciones) if descripciones else 0
    }
    return analisis

def guardar_en_excel(analisis, nombre_archivo):
    wb = Workbook()
    ws = wb.active
    ws.title = "Análisis"

    ws.append(["Métrica", "Valor"])
    for clave, valor in analisis.items():
        ws.append([clave, valor])

    nombre_excel = nombre_archivo + ".xlsx"
    wb.save(nombre_excel)
    print(f"Resultados guardados en: {nombre_excel}")

def graficar(medicamentos, nombre_archivo):
    nombres = [m['name'] for m in medicamentos]
    longitudes = [len(m['description']) for m in medicamentos]

    plt.figure(figsize=(10, 5))
    plt.bar(nombres, longitudes, color='teal')
    plt.xticks(rotation=45, ha='right')
    plt.title("Longitud de la descripción por medicamento")
    plt.ylabel("Caracteres")
    plt.tight_layout()
    plt.savefig(nombre_archivo + "_grafico.png")
    print(f"Gráfico guardado como {nombre_archivo}_grafico.png")
    plt.show()

def main():
    if len(sys.argv) < 3:
        print("Uso: python analisis_visualizacion.py archivo.csv nombre_salida")
        sys.exit(1)

    archivo_csv = sys.argv[1]
    nombre_salida = sys.argv[2]

    if not validar_nombre_archivo(nombre_salida):
        print("Nombre de archivo inválido. Usa solo letras, números, guiones o guiones bajos.")
        sys.exit(1)

    medicamentos = cargar_datos(archivo_csv)
    analisis = analizar_medicamentos(medicamentos)
    guardar_en_excel(analisis, nombre_salida)
    graficar(medicamentos, nombre_salida)

if __name__ == "__main__":
    main()
