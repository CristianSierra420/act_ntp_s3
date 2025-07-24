### Con un ciclo for, imprime la tabla de multiplicar del 7, es decir, 7 × 1, 7 × 2, …, 7 × 10, cada resultado en una línea.

for i in range(1, 11):
    resultado = 7 * i
    print(f"7 X {i} = {resultado}")