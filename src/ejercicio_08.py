### Usando un ciclo while, calcula y muestra los cuadrados de los números del 1 al 20 (1², 2², …, 20²), cada resultado en una línea.

i = 1
while i <= 20:
    cuadrado = i ** 2
    print(f"{i}² = {cuadrado}")
    i += 1