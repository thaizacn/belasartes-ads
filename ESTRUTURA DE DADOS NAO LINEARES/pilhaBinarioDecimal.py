'''
TESTE DE MESA

Digite um número decimal: 2002

Pilha vazia: 
pilha = []
O primeiro resto é adicionado à pilha: 
resto = 0
pilha = [0]
O segundo resto é adicionado à pilha: 
resto = 1
pilha = [0, 1]
O terceiro resto é adicionado à pilha: 
resto = 0 
pilha = [0, 1, 0]
O quarto resto é adicionado à pilha: 
resto = 0
pilha = [0, 1, 0, 0]
O quinto resto é adicionado à pilha: 
resto = 1
pilha = [0, 1, 0, 0, 1]
O sexto resto é adicionado à pilha: 
resto = 0
pilha = [0, 1, 0, 0, 1, 0]
O sétimo resto é adicionado à pilha: 
resto = 0
pilha = [0, 1, 0, 0, 1, 0, 0]
O oitavo resto é adicionado à pilha: 
resto = 1
pilha = [0, 1, 0, 0, 1, 0, 0, 1]
Entra no "for" que varre de trás para frente e cada valor é adicionado à string binario, na ordem inversa: 
binario = "11111010010"

O número 2002 em binário é 11111010010.

'''

def decimal_para_binario(decimal):
    pilha = []

    while decimal > 0: #Executa ENQUANTO o valor de decimal for maior que zero
        resto = decimal % 2 #Calculando o resto da divisão do decimal por dois e guardando o resto
        pilha.append(resto) #O resto da divisão inteira é adicionado na pilha 
        decimal //= 2 #Atualizando o valor de decimal com a divisão inteira por 2

    binario = ''
    for i in range(len(pilha) - 1, -1, -1): #Percorrendo a lista de restos
    #O laço começando do último índice da lista (len(pilha) - 1) até o primeiro índice (-1), com incrementos de -1 em -1 (-1).
        binario += str(pilha[i]) #Em cada iteração, o valor do resto correspondente ao índice i é adicionado à direita da string binario.

    return binario

decimal = int(input("Digite um número decimal: "))
binario = decimal_para_binario(decimal)
print(f"O número {decimal} em binário é {binario}.")
