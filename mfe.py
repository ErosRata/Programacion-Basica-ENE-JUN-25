import statistics
lista = [5.7, 5.8, 5.9, 6.5, 7.3, 7.4, 7.6, 8.1, 8.1, 8.9]

media = statistics.mean(lista)
varianza = statistics.variance(lista)
des = statistics.stdev(lista)
coe = (statistics.stdev(lista) / statistics.mean(lista)) * 100
print(media)
print(varianza)
print(des)
print(coe)