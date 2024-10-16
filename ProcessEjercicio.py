import multiprocessing
from time import time

# Función para calcular Fibonacci
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

# Función que ejecuta el cálculo de Fibonacci en un proceso
def calcular_fibonacci_en_proceso(vector, idx):
    vector[idx] = fibonacci(vector[idx])

def main():
    vector = multiprocessing.Array('i', [33] * 144)
    processes = []
    ts = time()
    
    for i in range(len(vector)):
        p = multiprocessing.Process(target=calcular_fibonacci_en_proceso, args=(vector, i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f"Vector procesado con procesos: {list(vector)}")
    print(f"Tardó {time() - ts} segundos")

if __name__ == "__main__":
    main()
