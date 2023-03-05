"""
-----------------------------------------
Desenvolva um algoritmo e um programa python que receba o ano atual e o ano de
nascimento de uma pessoa e mostre a idade dela no ano atual.

+

Desenvolva um algoritmo que recebe o ano de nascimento de uma pessoa e o ano atual, calcula e mostra a idade desta pessoa 
e quantos anos essa pessoa terá daqui a 10 anos.

Algoritmo IdadeAtual
inicio
  Declarar
    AnoAtual inteiro;
    AnoNascimento inteiro;

  //Entrada de dados
  escrever("Digite o ano em que estamos:  "); 
  ler(AnoAtual); 
  escrever("Digite o ano em que você nasceu:  "); 
  ler(AnoNascimento); 

  //Processamento de dados
  Idade = AnoAtual - AnoNascimento

  CASO QUEIRA SABER A IDADE EM 10 ANOS:
  NovaIdade = Idade + 10

  //Saída dos resultados
  escrever ("Sua idade após seu aniversário desse ano será" + Idade);

fim
-----------------------------------------
"""

import decimal 

AnoAtual = decimal.Decimal(input("Digite o ano em que estamos: "))
AnoNascimento = decimal.Decimal(input("Digite o ano em que você nasceu: "))

Idade = AnoAtual - AnoNascimento;

print (f"\nSua idade após seu aniversário desse ano será: {Idade}.")

DezAnos = input("\nDeseja saber quantos anos terá em 10 anos? RESPONDA SIM OU NÃO: ")

if(DezAnos == "SIM"):
  NovaIdade = Idade + 10
  print(f"Sua idade daqui 10 anos será: {NovaIdade}")
else:
  print("Puxa, quem sabe da próxima!")
