import os
import msvcrt

def persona_vs_persona():
    borrarPantalla = lambda: os.system("cls")
    borrarPantalla()
    borrarPantalla()
    print("==================================")
    print("========Adivina la palabra========")
    print("========Persona Vs Persona========")
    print("==================================\n")
    nom_of_palabrero = input("Introduce el nombre de la persona que escribirá la palabra: ")
    nom_of_palabrero = nom_of_palabrero.title()
    nom_of_palabrero = nom_of_palabrero.split()[0]
    print(f"{nom_of_palabrero},tu debes ingresar la palabra secreta.")
    print("Antes de que ingreses la palabra debo decirte algo")
    print("Si ingresas mas de una palabra, borrare la segunda palabra")
    while True:
        try:
            palabrasecret = input("Ahora ingresa una palabra: ")
            palabrasecret = palabrasecret.strip()
            if palabrasecret.isalpha():
                break
            else:
                print("Introduce solo letras")
        except ValueError:
            print("Error: Vuelva a intentarlo")
    palabrasecret = palabrasecret.split()[0]
    palabrasecret = palabrasecret.title()
    print("Presiona enter")
    msvcrt.getch()
    borrarPantalla()
    nom_of_pleyer = input("Cual es el nombre del adivinador o adivinadora: ")
    nom_of_pleyer = nom_of_pleyer.title()
    print(f"{nom_of_pleyer}, tú eres la persona que se encargara de descrubrir la palabra secreta\n")
    print("Tienes tres intentos")
    partes = [palabrasecret[i:i+len(palabrasecret)//3] for i in range(0, len(palabrasecret), len(palabrasecret)//3)]
    parte1 = partes[0]
    parte2 = partes[1]
    parte3 = partes[2]
    cont = 0
    while True:
        palabraintro = input("Introduce la palabra para adivinarla: ")
        palabraintro = palabraintro.title()
        if palabraintro == palabrasecret:
            break
        else:
            cont += 1
            if cont == 1:
                print("Te dare una pista")
                print(parte1)
            elif cont == 2:
                print("Te quedan 2 intentos")
                print(parte2)
            elif cont == 3:
                print("Solo te queda un ultimo intento")
                print(f"Esta es la ultima pista {parte3}")
            else:
                break
    if palabraintro == palabrasecret:
        print(f"{nom_of_pleyer} ganaste. Adivinaste la palabra {palabrasecret}")
    else:
        print(f"Perdiste. La palabra era {palabrasecret}")
persona_vs_persona()