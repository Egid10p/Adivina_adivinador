import random

def numeros_vs_maquina():
    print("===============================")
    print("=======Adivina el numero=======")
    print("=======Persona Vs Maquina======")
    print("===============================\n")
    while True:
        try:
            nom = int(input("¿Cual es el numero maximo posible?: "))
            break
        except ValueError:
            print("Error: Debe introducir un valor entero")
    numerosecret = random.randint(1, nom)
    cont = 1
    while True:
        try:
            numintro = int(input("Cual crees que es el numero entero: "))
            if numintro > numerosecret:
                print(f"{numintro} es mayor al numero secreto intenta reducir el numero")
            elif numintro < numerosecret:
                print(f"{numintro} es menor al numero secreto intenta aumentar el numero")
            elif numintro == numerosecret:
                break
            if numintro != numerosecret:
                cont += 1
        except ValueError:
            print("Error: introduce un numero entero")
    print("Ganaste")
    if cont == 1:
        print("En el primer intento")
    else:
        print(f"En {cont} intentos")