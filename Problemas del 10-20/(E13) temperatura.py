tipo = int(input('Que tipo de temperatura vas a convertir (celsius=1), (fahrenheit=2), (kelvin=3): '))
F = []
K = []
if tipo == 1:
    C = float(input('Introduce la cantidad a convertir: '))
    F = (C * 1.8) + 32
    K = C + 273.15
else: print('En fahrenheit:', F, 'y en Kelvin:', K)