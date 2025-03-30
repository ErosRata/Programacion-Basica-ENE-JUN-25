frase = input("Introduce lo que sea: ")
frase = frase.lower()
frase = frase.replace(".", "").replace(",", "").replace("!", "").replace("?", "")

palabras = frase.split()
print("El numero total de palabras en el texto:", len(palabras))

palabras_unicas = list(set(palabras))
print("La cantidad de palabras unicas:", len(palabras_unicas))

frecuencia = {}
for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1
print("La frecuencia de cada palabra:", frecuencia)

mas_veces = palabras_unicas[0]
for palabra in palabras_unicas[1:]:
    if frecuencia[mas_veces] < frecuencia[palabra]:
        mas_veces = palabra
print(
    "La palabras mas frecuente:",
    mas_veces,
    "y cuantas veces aparece:",
    frecuencia[mas_veces],
)
