### Utilizando un ciclo while, calcula el factorial de un número entero n introducido por el usuario y muestra el resultado.

numero = int(input("ingrese un numero para calcular su factorial:"))
factorial = 1
contador = 1
while contador <= numero:
    factorial *= contador
    contador += 1
print(f"El factorial de {numero} es: {factorial}")