C = float(input("Introduce el capital invertido: "))
r = float(input("Introduce la tasa (en porcentaje): "))
t = float(input("Introduce el tiempo: "))

monto_final = C * (1 + r) ** t
print("El monto final es de:",monto_final)