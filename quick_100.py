import random
import time


# Algoritmo Quick Sort
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


# Tamanhos definidos na sua tabela
tamanhos = [100, 1000, 10000, 100000, 1000000, 10000000]

print(f"{'Tamanho':>12} | {'Tempo (s)':>10}")
print("-" * 26)

for tamanho in tamanhos:
    arr = [random.randint(1, 10000000) for _ in range(tamanho)]

    inicio = time.perf_counter()
    quicksort(arr, 0, len(arr) - 1)
    fim = time.perf_counter()

    tempo = fim - inicio
    print(f"{tamanho:>12} | {tempo:>10.6f}")