tipo = input("Introduce la medida a calcular ya sea area o volumen (Area = A, a, 1; Volumen = V, v. 2): ")

if tipo == 'A' or tipo == 'a' or tipo == '1':
    area = input("Introduce la figura a calcular (Cuadrado = c, circulo = o, triangulo = t): ")
    if area == 'c':
        longitud = float(input("Introduce la longitud del cuadrado: "))
        areac = longitud ** 2
        print(areac)
    elif area == 'o':
        radio = float(input("Introduce el radio del circulo: "))
        areac = 3.1416 * (radio ** 2)
        print(areac)
    elif area == 't':
        b = float(input("Introduce la base: "))
        h = float(input("Introduce la altura: "))
        areac = (b * h)/2
        print(areac)
    else:
        print("Escoje bien")
elif tipo == 'V' or tipo == 'v' or tipo == '2':
    volumen = input("Introduce el volumen a calcular (Cubo = c, Esfera = o Cilindrio = u): ")
    if volumen == 'c':
        longitud = float(input("Introduce la longitud del cubo: "))
        volumenc = longitud ** 3
        print(volumenc)
    elif volumen == 'o':
        radio = float(input("Introduce el radio de la esfera: "))
        volumenc = (4/3) * 3.1416 * (radio ** 3)
        print(volumenc)
    elif volumen == 'u':
        r = float(input("Introduce el radio del cilindro: "))
        h = float(input("Introduce la altura del cilindro: "))
        volumenc = (3.1416 * h) * (r ** 2)
        print(volumenc)
    else:
        print("Escoja bien")
else:
    print("Que menso no escojes bien")