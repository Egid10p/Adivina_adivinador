import os
import msvcrt
def numero_vs_persona():
    borrarPantalla = lambda: os.system("cls")
    borrarPantalla()
    borrarPantalla()
    print("===============================")
    print("=======Adivina el numero=======")
    print("=======Persona Vs Persona======")
    print("===============================\n")

    nomnumero = input("Cual es el nombre de la persona que introducira el numero: ")
    nomnumero = nomnumero.split()[0].title()
    while True:
        try:
            numerosecret = int(input(f"{nomnumero} tu debes ingresar un numero secreto positivo: "))
            if numerosecret > 0:
                break
            else:
                print("Error: Debes ingresar un numero entero positivo")
        except ValueError:
            print("Error: Debes ingresar un numero entero")
    print("Presiona enter")
    msvcrt.getch()
    borrarPantalla()
    cont = 1
    nomplayer = input("¿Cual es el nombre del jugador?: ")
    nomplayer = nomplayer.split()[0].title()
    while True:
        try:
            numintro = int(input(f"¿{nomplayer} cual crees que es el numero entero?: "))
            if numintro > numerosecret:
                print(f"{numintro} es mayor al numero secreto intenta reducir el numero\n")
            elif numintro < numerosecret:
                print(f"{numintro} es menor al numero secreto intenta aumentar el numero\n")
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