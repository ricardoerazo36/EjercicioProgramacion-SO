from threading import Thread
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

# Clase para trabajador con hilos
class FiboWorker(Thread):
    def __init__(self, vector, idx):
        Thread.__init__(self)
        self.vector = vector
        self.idx = idx

    def run(self):
        self.vector[self.idx] = fibonacci(self.vector[self.idx])

def main():
    vector = [33] * 144
    hilos = []
    ts = time()
    
    for i in range(len(vector)):
        worker = FiboWorker(vector, i)
        worker.start()
        hilos.append(worker)

    for hilo in hilos:
        hilo.join()

    print(f"Vector procesado con hilos: {vector}")
    print(f"Tardó {time() - ts} segundos")

if __name__ == "__main__":
    main()
