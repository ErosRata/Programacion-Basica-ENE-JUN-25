import requests
import csv
import re

def validar_sintoma(sintoma):
    patron = r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]{3,50}$"
    return re.match(patron, sintoma) is not None

sintoma = input("Ingresa tu síntoma (ej. dolor de cabeza): ").strip()

if not validar_sintoma(sintoma):
    print("Entrada inválida. Usa solo letras y espacios.")
    exit()

url = f"https://api.api-ninjas.com/v1/drug?name={sintoma}"
headers = {'X-Api-Key': 'SQi2iFURR0HZUMPvEc+rew==NXO7vBBuf4SMPefK'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    if not data:
        print("No se encontraron medicamentos para ese síntoma.")
    else:
        with open("medicamentos.csv", mode="w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["Nombre", "Categoría"])
            for item in data:
                writer.writerow([item.get("name", "Desconocido"), item.get("category", "No disponible")])
        print("Datos guardados en medicamentos.csv")
else:
    print("Error al consultar la API:", response.status_code)