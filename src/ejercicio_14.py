### Mediante un ciclo while, implementa un juego de adivinanza: el programa genera un número aleatorio del 1 al 10 y solicita al usuario que lo adivine. El proceso se repite hasta que el usuario acierte. Muestra un mensaje de felicitación al final.

import random

numero_aletorio = random.randint(1, 10)
adivinado = False
while not adivinado:
    intento = int(input("Adivina el número (del 1 al 10): "))
    if intento == numero_aletorio:
        print("¡Felicidades! Has adivinado el número.")
        adivinado = True
    else:
        print("Inténtalo de nuevo.")
        adivinado = False
