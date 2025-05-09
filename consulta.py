import re
import csv
import requests
import time

def validar_sintoma(sintoma):
    patron = r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]{3,50}$'  
    return re.match(patron, sintoma.strip()) is not None

def buscar_medicamentos(sintoma):
    url = "https://api.api-ninjas.com/v1/drug?name=" + sintoma.lower()
    headers = {'X-Api-Key': 'SQi2iFURR0HZUMPvEc+rew==NXO7vBBuf4SMPefK'}
    try:
        respuesta = requests.get(url, headers=headers)
        if respuesta.status_code == 200:
            return respuesta.json()
        else:
            print(f"Error en la API ({respuesta.status_code}): {respuesta.text}")
            return []
    except requests.exceptions.RequestException as e:
        print("Error de conexión:", e)
        return []

def guardar_en_csv(medicamentos, sintoma):
    nombre_archivo = f"medicamentos_{sintoma.lower()}.csv"
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
        campos = ['name', 'description']
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for m in medicamentos:
            escritor.writerow({
                'name': m.get('name', 'Desconocido'),
                'description': m.get('description', 'Sin descripción disponible')
            })
    print(f"Datos guardados en: {nombre_archivo}")

def main():
    print("SISTEMA DE CONSULTA FARMACÉUTICA")
    sintoma = input("Ingrese un síntoma:").strip()

    if not validar_sintoma(sintoma):
        print("Entrada inválida. Solo letras, sin números o símbolos.")
        return

    print(f"Buscando medicamentos relacionados con: {sintoma}...")
    medicamentos = buscar_medicamentos(sintoma)

    if medicamentos:
        guardar_en_csv(medicamentos, sintoma)
    else:
        print("No se encontraron resultados. Consulte a su médico.")

if __name__ == "__main__":
    main()
