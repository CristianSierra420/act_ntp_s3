### Con un ciclo for, cuenta cuántas vocales (sin distinción de mayúsculas/minúsculas) hay en la frase frase = "programacion es divertida" y muestra el total.

vocales = "aeiouáéíóú"
frase = "nacional es campeon de copa libertadores"
contador = 0
frase = frase.lower()  # Convertir la frase a minúsculas para facilitar la comparación
for letra in frase:
    if letra in vocales:
        contador += 1
print(f"El total de vocales en la frase es: {contador}")