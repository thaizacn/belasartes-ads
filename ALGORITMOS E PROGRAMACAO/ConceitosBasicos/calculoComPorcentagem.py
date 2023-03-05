'''
-----------------------------------------

Desenvolva um algoritmo e um programa python que receba o valor do salário 
de um colaborador, calcula e mostra o seu novo salário com um reajuste de 23%.

Algoritmo CalculoSalario
inicio
  Declarar
    SalarioAtual inteiro;

  //Entrada de dados e o processamento dos dados
  escrever("Digite seu salário: "); //essa mensagem aparece na tela do usuário
  ler(SalarioAtual); // o que o usuário digitar, é armazenado na variável SalarioAtual 

  //Processamento de dados
  SalarioAtual * 23%

  //Saída dos resultados
  escrever ("O seu salario atual" + SalarioAtual + ", com o reajuste irá para " + Resultado);

fim
-----------------------------------------
'''

import decimal

SalarioAtual = decimal.Decimal(input("Digite o seu salario: "))
Reajuste = decimal.Decimal(input("Digite o numéro da porcentagem do reajuste: "))

Por = SalarioAtual / 100
Reaj = Por * Reajuste;
Resultado = SalarioAtual + Reaj;
print (f"\nO seu salario atual {SalarioAtual} com o reajuste irá para {Resultado}.")

'''
-----------------------------------
Desenvolva um algoritmo que recebe o salário bruto de um funcionário, calcula e mostra o salário líquido deste funcionário, 
sabendo que ele recebe 10% de gratificação calculados sobre o salário bruto, mas paga 20% de imposto de renda também calculados 
sobre o salário bruto.

Algoritmo IdadeAtual
inicio
  Declarar
    Salario inteiro;

  //Entrada de dados
  escrever("Digite o valor do seu salário bruto:  "); 
  ler(Salario); 

  //Processamento de dados
  Porcentagem = Salario / 100
  SalarioLiquido = Porcentagem - 10

  //Saída dos resultados
  escrever ("Seu salário líquido é de" + SalarioLiquido);

fim
-----------------------------------
'''

import decimal

Salario = decimal.Decimal(input("Digite o seu salário: "))

Porcentagem = Salario / 100
SalarioLiquido = Porcentagem * 10
Resultado = Salario - SalarioLiquido;

print(f"Seu salário líquido é {Resultado}")

'''
-------------------------------
Desenvolva um algoritmo que recebe o valor de um depósito em poupança, calcula e mostra o valor após 
um mês de aplicação na poupança, sabendo que a poupança rende 5% ao mês.

Algoritmo Poupança
inicio
  Declarar
    ValorDeposito inteiro;

  //Entrada de dados e o processamento dos dados
  escrever("Quanto você deseja depositar hoje? "); 
  ler(ValorDeposito); 

  //Processamento de dados
  Porcentagem = 5 / 100 * ValorDeposito

  //Saída dos resultados
  escrever ("Seu dinheiro renderá em um mês um total de:" + Porcentagem);

fim
-------------------------------
'''

import decimal 

ValorDeposito = float(input("Quanto você deseja depositar hoje? "))

Porcentagem = 5 / 100 * ValorDeposito
Resultado = ValorDeposito + Porcentagem

print(f"Seu dinheiro renderá em um mês um total de: {Resultado}")