import random

jugar = input("Cual juego quieres jugar? (Moneda = M, m o 1; Dado = D, d o 2): ")
numero = []

if jugar == 'M' or jugar == 'm' or jugar == '1':
    numero = random.randrange(1,2)
    if numero == 1:
        print("Aguila")
    else:
        print("Sol")
else:
    jugar == "D" or jugar == 'd' or jugar == '2'
    numero = random.randrange(1,6)
    print(numero)