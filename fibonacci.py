# Función para calcular el número de Fibonacci de manera secuencial
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Inicializamos el vector de longitud 144 con el valor 33 en cada posición
vector = [33] * 144

# Procesamos cada posición del vector para calcular el Fibonacci de cada valor
for i in range(len(vector)):
    vector[i] = fibonacci(vector[i])

# Mostramos el resultado final del vector
print("Vector procesado con valores de Fibonacci (secuencial):")
print(vector)
