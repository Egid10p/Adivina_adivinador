import Volver_a_ejecutar
while True:
    Volver_a_ejecutar.programa()
    while True:
        desci = input("¿Quiere volver a ejecutar el programa?(s/n): ")
        if desci.lower() == "s" or desci.lower() == "n":
            break
        else:
            print("Error")
    if desci.lower() == "n":
        break