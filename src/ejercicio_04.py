### Utilizando un ciclo while, solicita al usuario que ingrese números. El proceso termina cuando el usuario escriba 0. Al final, muestra la suma total de todos los números ingresados.

suma_total = 0
while True:
    numero = int(input("ingrese un numero (0 para terminar el ciclo):"))
    if numero == 0:
        break
    suma_total += numero
print("La suma total de los números ingresados es:", suma_total)