### Usando un ciclo while, calcula y muestra los cuadrados de los números del 1 al 20 (1², 2², …, 20²), cada resultado en una línea.

calcula = 1
while calcula <= 20:
    cuadrado = calcula ** 2
    print(f"{calcula}² = {cuadrado}")
    calcula += 1