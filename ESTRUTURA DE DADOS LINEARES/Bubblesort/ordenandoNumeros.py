def bubble_sort(arr):
    n = len(arr)
    trocou = True
    while trocou:
        trocou = False
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                trocou = True
    return arr

# Recebendo o input do usuário
entrada = input("Digite os números separados por espaço: ")

# Convertendo a entrada em um array de números inteiros
numeros = [int(num) for num in entrada.split()]

numeros_ordenados = bubble_sort(numeros)
print(f"Os números digitados ordenados: {numeros_ordenados}")