'''
-----------------------------------------
Desenvolva um algoritmo que recebe os valores a, b e c de uma equação de segundo grau (ax2 + bx + c), 
calcula e mostra as raízes reais desta equação, considerando uma equação que possui duas raízes reais
-----------------------------------------
'''

import math 

Abc = input("Digite o valor de A, B e C respectivamente separados por vírgula: ")

A, B, C = Abc.split(",")
A, B, C = int(A), int(B), int(C)

Delta = (B ** 2) - 4 * A * C

if(Delta < 0):
    print("Delta é menor que 0, não há raizes!")
elif(Delta > 0):
    X1 = -(B - math.sqrt(Delta)) / (2 * A)
    X2 = -(B + math.sqrt(Delta)) / (2 * A)
    print(f"O valor da primeira raiz é: {X1} e da segunda: {X2}")
else:
    X1 = -(B + math.sqrt(Delta)) / (2 * A)
    print(f"Essa equação só possui uma raiz que é igual a: {X1}")
