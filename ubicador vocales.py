def ubicadorDeVocales(palabra):
    ubicacion = {}
    vocales = "aeiouáéíóú"
    for indice, i in enumerate(palabra.lower()):
        if i in vocales:
            if i in ubicacion:
                ubicacion[i].append(indice)
            else:
                ubicacion[i] = [indice]
    return ubicacion

print(ubicadorDeVocales("murciélago"))
print(ubicadorDeVocales("eucalipto"))
print(ubicadorDeVocales("Albericoque"))