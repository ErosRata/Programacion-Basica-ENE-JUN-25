def contadorDeVocales(palabra):
    contador = {}
    vocales = "aeiouáéíóú"
    for i in palabra.lower():
        if i in vocales:
            if i in contador:
                contador[i] +=1
            else:
                contador[i] = 1
    return contador

print(contadorDeVocales("murciélago"))
print(contadorDeVocales("eucalipto"))
print(contadorDeVocales("Albericoque"))