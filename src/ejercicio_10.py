### Mediante un ciclo while, solicita al usuario que escriba palabras. El proceso termina cuando el usuario escriba la palabra “fin”. Al final, muestra cuántas palabras se leyeron (sin contar “fin”).

contador_palabras = 0
while True:
    palabra = input("Escribe una palabra(o fin para terminar el ciclo):")
    if palabra.lower() == "fin":
        break
    contador_palabras += 1
print(f"Se leyeron {contador_palabras} palabras.")