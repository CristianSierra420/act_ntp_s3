### Utilizando un ciclo while, solicita al usuario que ingrese edades una a una. El proceso termina cuando se introduzca -1. Al final, muestra la edad mayor que se haya ingresado.

edad_mayor = -1 # Inicializamos con -1 para indicar que aún no se ha ingresado una edad válida

while True:
    edad = int(input("Ingrese su edad (para salir ingrese -1): "))
    
    if edad == -1:
        print("No se ingresó una edad válida.")
        break

    if edad <= 0:
        print("Edad no aprobada. Debe ser mayor que 0.")
        continue  

    edad_mayor = edad
    print(f"La edad ingresada es válida: {edad_mayor}")
    break  
print(f"La edad mayor ingresada es: {edad_mayor}")
