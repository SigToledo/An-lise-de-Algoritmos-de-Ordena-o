import random
import time

TAMANHO = 10000000

def quicksort(arr, inicio, fim):
    if inicio < fim:
        p = particiona(arr, inicio, fim)
        quicksort(arr, inicio, p - 1)
        quicksort(arr, p + 1, fim)

def particiona(arr, inicio, fim):
    pivo = arr[fim]
    i = inicio - 1
    for j in range(inicio, fim):
        if arr[j] < pivo:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[fim] = arr[fim], arr[i + 1]
    return i + 1

arr = [random.randint(1, 100000000) for _ in range(TAMANHO)]
#print(f"\n Vetor original (N={TAMANHO}):")
#print(arr)

inicio = time.perf_counter()
quicksort(arr, 0, len(arr) - 1)
fim = time.perf_counter()

#print(f"\n Vetor ordenado:")
#print(arr)

print(f"\n Tempo: {fim - inicio:.6f} segundos\n")