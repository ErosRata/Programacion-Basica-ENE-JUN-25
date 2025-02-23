dinero = float(input("Introduce la cantidad actual de dinero total: "))

accion = input("Que desea realizar un retiro(R, r, 1) o un deposito(D, d, 2): ")

if accion == 'R' or accion == 'r' or accion == '1':
    retiro = float(input("Introduce la cantidad a retirar: "))
    monto_actual = dinero - retiro
elif accion == 'D' or accion == 'd' or accion == '2':
    deposito = float(input("Introduce la cantidad a depositar: "))
    monto_actual = dinero + deposito
else:
    print("Escribe bien pa")

print("El monto actual despues de la accion es de:", monto_actual)