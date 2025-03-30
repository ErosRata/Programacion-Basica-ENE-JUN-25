import conversor

accion = input(
    "Que quieres convertir distancia(1, d, D), temperatura(2, t, T) o liquidos(3, l, L): "
)

if accion == "1" or accion == "d" or accion == "D":
    km = float(input("Introduce un valor a convertir: "))
    print(conversor.Kms_to_mile(km))
elif accion == "2" or accion == "t" or accion == "T":
    c = float(input("Introduce un valor a convertir: "))
    print(conversor.Cel_to_Faren(c))
elif accion == "3" or accion == "l" or accion == "L":
    lts = float(input("Introduce un valor a convertir: "))
    print(conversor.Lts_to_Gal(lts))
else:
    print("Escoje bien pa")