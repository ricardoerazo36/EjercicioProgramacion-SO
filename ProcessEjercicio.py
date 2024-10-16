from time import time
import multiprocessing
import sys

# Función para calcular el número de Fibonacci
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

# Clase para trabajadores utilizando procesos
class FiboWorker(multiprocessing.Process):
    def __init__(self, vector, idx, pid):
        multiprocessing.Process.__init__(self)
        self.vector = vector
        self.idx = idx
        self._pid = pid

    def run(self):
        print(f"[{self._pid}] Calculando Fibonacci de {self.vector[self.idx]}")
        self.vector[self.idx] = fibonacci(self.vector[self.idx])
        print(f"[{self._pid}] Fibonacci calculado es {self.vector[self.idx]}")

def main():
    # Definir el tamaño del vector y el valor inicial
    vector_size = 144
    initial_value = 33
    if len(sys.argv) > 1:
        vector_size = int(sys.argv[1])
    num_cpus = multiprocessing.cpu_count()  # CPUs disponibles
    print(f"Calculando Fibonacci para {vector_size} posiciones en {num_cpus} CPUs")

    # Inicializamos el vector de longitud `vector_size` con el valor `initial_value`
    vector = multiprocessing.Array('i', [initial_value] * vector_size)
    procesos = []  # Vector de procesos

    ts = time()  # Se toma el tiempo
    for i in range(vector_size):
        pid = i % num_cpus  # Asignar IDs de proceso basado en el número de CPUs
        worker = FiboWorker(vector, i, pid)
        print(f"Trabajador {i} comienza para la posición {i}")
        worker.start()
        procesos.append(worker)

    for i in range(vector_size):  # Ciclo para esperar por los trabajadores
        print(f"Esperando por trabajador {i}")
        procesos[i].join()

    print(f"Vector procesado: {list(vector)}")
    print(f"Tardó {time() - ts} segundos")

if __name__ == "__main__":
    main()
