def palindromo(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace(" ","") 
    a = 0
    b = len(palabra) - 1

    for i in range(0, len(palabra)):
        if palabra[a] == palabra[b]:
            a += 1
            b -= 1
        else: 
            return False
    return True

palabra = input("Ingrese una frase o palabra: ")
if palindromo(palabra):
    print("es palindromo")
else:
    print("NO es palindromo")