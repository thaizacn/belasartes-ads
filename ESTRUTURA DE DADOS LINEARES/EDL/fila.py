class Fila:
    def __init__(self):
        self.items = []

    def enfileirar(self, item):
        self.items.append(item)

    def desenfileirar(self):
        if not self.esta_vazia():
            return self.items.pop(0)

    def esta_vazia(self):
        return len(self.items) == 0


def binario_para_decimal(numero_binario):
    fila_binario = Fila()
    decimal = 0
    posicao = 0

    # Enfileira cada dígito binário da direita para a esquerda
    for digito in numero_binario[::-1]:
        fila_binario.enfileirar(int(digito))

    # Realiza a conversão para decimal
    while not fila_binario.esta_vazia():
        digito = fila_binario.desenfileirar()
        decimal += digito * (2 ** posicao)
        posicao += 1

    return decimal


# Teste de mesa para a entrada com o número 2002 em binário
numero_binario = '11111010010' #2002 em Binário
numero_decimal = binario_para_decimal(numero_binario)
print(f'O número binário {numero_binario} é igual a {numero_decimal} em decimal.')

'''
Posição     |  10  |   9  |   8  |   7  |   6  |   5  |   4  |   3  |   2  |   1  |   0  |
----------------------------------------------------------------------------------------
Número      |   1  |   1  |   1  |   1  |   1  |   0  |   1  |   0  |   0  |   1  |   0  |
----------------------------------------------------------------------------------------
Decimal     | 1024|  512|  256|  128|   64|   0  |   16|   0  |   0  |   2  |   0  |
----------------------------------------------------------------------------------------
'''