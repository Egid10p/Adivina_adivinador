import random

def adivina_vs_maquina():
    print("==============================")
    print("======Adivina la palabra======")
    print("======Persona Vs Maquina======")
    print("==============================\n")
    listpalabras = "Bailar", "Correr", "Viajar", "Cocinar", "Libro", "Guitarra", "Pelicula", "Serie", "Videojuego", "Pintar", "Abogado", "Taxista", "Actriz", "Piloto", "Profesor", "Enfermera", "Doctor", "Veterinaria", "Albañil", "Panaderia", "Biblioteca", "Peluqueria", "Hospital", "Parque", "Zapateria", "Futbol", "Tenis", "Baloncesto", "Voleibol", "Natacion", "Atletismo", "Esqui", "Pantalon", "Vaquero", "Falda", "Vestido", "Abrigo", "Blusa", "Calcetines", "Sudadera", "Cinturon", "Collar", "Anillo", "Pulsera", "Bolso", "Reloj", "Gafas", "Sombrero", "Gorra"
    numlist = len(listpalabras)
    palabrasecret = listpalabras[random.randint(0, numlist-1)]
    nomplayer = input("Cual es tu nombre: ")
    nomplayer = nomplayer.title()
    nomplayer = nomplayer.split()[0]
    print(f"{nomplayer} tienes tienes que adivinar la palabra secreta")
    print("Tienes tres intentos")
    print("Nota: Todas la palabras introducidas por la maquina son en singular")
    partes = [palabrasecret[i:i+len(palabrasecret)//3] for i in range(0, len(palabrasecret), len(palabrasecret)//3)]
    parte1 = partes[0]
    parte2 = partes[1]
    parte3 = partes[2]
    cont = 0
    while True:
        palabraintro = input("Ingresa la palabra secreta: ")
        palabraintro = palabraintro.title()
        if palabraintro == palabrasecret:
            break
        else:
            print("Te equivocaste")
            cont = cont + 1
            if cont == 1:
                print("Te dare una pista")
                print(parte1)
            elif cont == 2:
                print("No te preocupes te dare otra pista pero solo te quedan dos intentos")
                print(parte2)
            elif cont == 3:
                print("Cuidado esta es tu ultima oportunidad y la ultima pista es esta")
                print(parte3)
            elif cont == 4:
                break
    if palabraintro == palabrasecret:
        print(f"{nomplayer} lograste adivinar la palabra {palabrasecret}")
    else:
        print(f"Lamento informarte que no edivinaste la palabra {palabrasecret}")