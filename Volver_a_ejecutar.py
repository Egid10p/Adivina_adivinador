def programa():
    print("============================")
    print("=====Adivina adivinador=====")
    print("============================\n")

    print("¿Que quieres jugar?")
    print("1.Adivina una palabra")
    print("2.Adivina un numero entero\n")

    while True:
        try:
            desci1 = int(input("Ingresa el numero correspondiente a la opción elegida: \n"))
            if desci1 < 3 and desci1 > 0:
                break
            else:
                print("Error: Opción no reconocida. Usted debe ingresar un numero entre 1 y 2")
        except ValueError:
            print("Error: Usted debe introducir un numero entero")

    if desci1 == 1:
        print("Ahora elige contra quien quieres jugar")
        print("1.Jugar contra una maquina")
        print("2.Jugar contra una persona")
        while True:
            try:
                desci2 = int(input("Intoduce el numero correspondiente a la opción elegida: \n"))
                if desci2 < 3 and desci2 > 0:
                    break
                else:
                    print("Error: Opción no reconocida. Usted debe ingresar un numero entre 1 y 2")
            except ValueError:
                print("Error: Usted debe introducir un numero entero")
        if desci2 == 1:
            import palabras_vs_maquina
            palabras_vs_maquina.adivina_vs_maquina()
        elif desci2 == 2:
            import palabras_vs_persona
            palabras_vs_persona.persona_vs_persona()
    elif desci1 == 2:
        print("Ahora elige contra quien quieres jugar")
        print("1.Jugar contra una maquina")
        print("2.Jugar contra una persona")
        while True:
            try:
                desci2 = int(input("Intoduce el numero correspondiente a la opción elegida: \n"))
                if desci2 < 3 and desci2 > 0:
                    break
                else:
                    print("Error: Opción no reconocida. Usted debe ingresar un numero entre 1 y 2")
            except ValueError:
                print("Error: Usted debe introducir un numero entero")
        if desci2 == 1:
            import numeros_vs_maquina
            numeros_vs_maquina.numeros_vs_maquina()
        elif desci2 == 2:
            import numeros_vs_persona
            numeros_vs_persona.numero_vs_persona()