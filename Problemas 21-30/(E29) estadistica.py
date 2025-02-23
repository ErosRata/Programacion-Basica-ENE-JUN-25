import statistics

datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

media = statistics.mean(datos)
mediana = statistics.median(datos)
moda = statistics.mode(datos)

print("Media:", media, "Mediana:", mediana, "Moda", moda)