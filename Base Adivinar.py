import random

def jugar_adivinanza():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("¡Bienvenido al juego de adivinanzas!")
    print("Estoy pensando en un número entre 1 y 100.")

    while True:
        intento = int(input("Introduce tu intento: "))
        intentos += 1

        if intento < numero_secreto:
            print("El número que estoy pensando es mayor que", intento)
        elif intento > numero_secreto:
            print("El número que estoy pensando es menor que", intento)
        else:
            print("¡Felicidades! ¡Adivinaste el número en", intentos, "intentos!")
            break

jugar_adivinanza()
