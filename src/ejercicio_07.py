### Con un ciclo for, cuenta cuántas letras “a” (minúscula) hay en la cadena texto = "manzana" y muestra el total.

texto = "manzana"
contador = 0
for letra in texto:
    if letra == 'a':
        contador += 1
print(f"El número de letras 'a' en '{texto}' es: {contador}")