### Con un ciclo for, solicita al usuario que ingrese un número entero positivo y calcula la suma de sus dígitos, mostrando el resultado final.

numero = input("Ingrese un numero positivo:")
suma_digitos = 0
for digitos in numero:
    if digitos.isdigit(): # Esto sirve para verificar si el caracter que mando es un dijito.
        suma_digitos += int(digitos)
        print(f"El digito {digitos} se suma a la suma total, que ahora es: {suma_digitos}")
print(f"La suma total de los dígitos de {numero} es: {suma_digitos}")