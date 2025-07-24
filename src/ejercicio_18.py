### Mediante un ciclo while, genera y muestra la secuencia de Fibonacci empezando por 1, 1, 2, 3, 5, … y termina cuando se alcance el primer valor mayor que 1000.

numero1 = 1
numero2 = 2
while numero1 <= 1000:
    print(numero1)
    numero1, numero2 = numero2, numero1 + numero2 # Esto actualiza los números de Fibonacci para la siguiente iteración
    if numero1 > 1000:
        break
print("Se ha alcanzado el primer valor mayor que 1000 en la secuencia de Fibonacci.")