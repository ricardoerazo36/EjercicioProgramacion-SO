from fibonacci import fibo

# Inicializamos el vector de longitud 144 con el valor 33 en cada posición
vector = [33] * 144

# Procesamos cada posición del vector para calcular el Fibonacci de cada valor
for i in range(len(vector)):
    vector[i] = fibo(vector[i])

# Mostramos el resultado final del vector
print("Vector procesado con valores de Fibonacci (secuencial):")
print(vector)
