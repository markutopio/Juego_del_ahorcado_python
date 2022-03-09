import random
import time

muneco_ahorcado = ['''


    +---+
    |   |
        |
        |
        |
        |
        ========''', '''


    +---+
    |   |
    O   |
        |
        |
        |
        ========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        ========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        ========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        ========''', '''


    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        ========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |

        ========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        ========''', '''

    ''']




lista = ["manopla", "teletrabajo", "raton", "animatronico", "router", "benceno", "integral", "servilleta",
         "capturadora", "pendrive", "comunismo", "republica", "aleatoriedad", "alfombrilla", "mujeriego",
         "hidrogenacion", "benzaldehido", "crossfit", "abdominales", "sarcofago"]

palabra_secreta_elegida = random.choice(lista)
numero_letras = len(palabra_secreta_elegida)
vidas = int(6)


print("¡Hola y bienvenido al juego del ahorcado!")
time.sleep(1)
print("Las reglas son sencillas, hay una palabra secreta que debes de averiguar, tienes 6 oportunidades, si fallas una letra pierdes una vida")
time.sleep(1)
print("TEN MUCHO CUIDADO CON LO QUE ELIGES")
time.sleep(1)


x= input("Escribe COMENZAR para arriesgarte a adivinar la palabra secreta")
p= True
time.sleep(0.8)
if x== "COMENZAR":




    while p== True:

        while p== True:
            letra_adivinada= input("Adivina una letra: ")

            if letra_adivinada== "resolver":
                resolver_la_palabra= input("¿Cual crees que es la palabra?")

                if  resolver_la_palabra == palabra_secreta_elegida:
                    print("¡Bien, has ganado!")
                    print("la palabra elegida era:" + palabra_secreta_elegida)
                    print("a continuación te enseño como habías dejado la partida")
                    time.sleep(1)
                    letra_adivinada= "hasta aquí el juego, puedes repetirlo cuantas veces quieras."
                    time.sleep(1)
                    print(letra_adivinada)
                    p= False
                    break
                if resolver_la_palabra == palabra_secreta_elegida.upper():
                    print("¡Bien, has ganado!")
                    print("la palabra elegida era:" + palabra_secreta_elegida)
                    print("a continuación te enseño como habías dejado la partida")
                    time.sleep(1)
                    letra_adivinada= "hasta aquí el juego, puedes repetirlo cuantas veces quieras."
                    time.sleep(1)
                    print(letra_adivinada)
                    p= False
                    break


            else:

                lista.append(letra_adivinada)


                if letra_adivinada in palabra_secreta_elegida:
                    print("Felicidades adivinaste una letra")
                    break

                else:
                    vidas = vidas - 1
                    print("Losiento, es incorrecto")
                    print("te quedan " + str(vidas) + " vidas")
                    break

        if vidas == 5:
            print("+---+")
            print("|   |")
            print("O   |")
            print("    |")
            print("    |")
            print("    |")
            print("     ========")
        if vidas == 4:
            print("+---+")
            print("|   |")
            print("O   |")
            print("|   |")
            print("    |")
            print("    |")
            print("     ========")
        if vidas == 3:
            print(" +---+")
            print(" |   |")
            print(" O   |")
            print("/|\  |")
            print("     |")
            print("     |")
            print("     ========")

        if vidas == 2:
            print("  +---+")
            print("  |    |")
            print("  O    |")
            print(" /|\   |")
            print("  |    |")
            print("       |")
            print("       ========")
        if vidas == 1:
            print("   +---+")
            print("   |     |")
            print("   O     |")
            print("  /|\    |")
            print("   |     |")
            print("    \    |")
            print("         ========")
        if vidas == 0:
            print("    +---+")
            print("    |     |")
            print("    O     |")
            print("   /|\    |")
            print("    |     |")
            print("   / \    |")
            print("          ========")


        if vidas== 0:
            print("Fallaste, aun así te doy la palabra: " + palabra_secreta_elegida)
            break


        estado_del_juego = ""

        letras_restantes= 0
        for letra in palabra_secreta_elegida:

            if letra in lista:
                estado_del_juego = estado_del_juego + letra

            else:
                estado_del_juego = estado_del_juego + "_"
                letras_restantes = letras_restantes + 1

        print(estado_del_juego)

        if letras_restantes == 0:
            print("¡Bien, has ganado!")
            print("la palabra elegida era:"+ palabra_secreta_elegida)
            p= False
            break

while p== False:
    break





