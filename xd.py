def suma_digitos(numero):
    suma = 0
    while numero > 0:
        digito = numero % 10
        suma += digito
        numero = numero // 10
    return suma

# Ejemplo de uso
numero = 12345
resultado = suma_digitos(numero)
print(f"La suma de los dígitos de {numero} es {resultado}")  # Salida: La suma de los dígitos de 12345 es 15
