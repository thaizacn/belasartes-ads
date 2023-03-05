'''
--------------------------------
Desenvolva um algoritmo que recebe um valor em Real, calcula e mostra o valor convertido para Dólar.

Algoritmo ConvertendoDolar
inicio
  Declarar
    ValorEmReal inteiro;

  //Entrada de dados e o processamento dos dados
  escrever("Digite o valor em Real: "); 
  ler(ValorEmReal); 

  //Processamento de dados
  ValoEmDolar = ValorEmReal / 5,06

  //Saída dos resultados
  escrever (ValorEmReal + "em doláres seria" + ValoEmDolar);

fim
--------------------------------
'''

ValorEmReal = float(input("Digite o valor em Real: "))

ValoEmDolar = ValorEmReal / 5.06

print(f"{ValorEmReal} em doláres seria {ValoEmDolar}")

'''
--------------------------------
Desenvolva um algoritmo que recebe um valor em Euro, calcula e mostra o valor convertido para Real.

Algoritmo ConvertendoDolar
inicio
  Declarar
    ValorEmReal inteiro;

  //Entrada de dados e o processamento dos dados
  escrever("Digite o valor em Euro: "); 
  ler(ValorEmEuro); 

  //Processamento de dados
  ValorEmReal = ValorEmEuro / 5,06

  //Saída dos resultados
  escrever (ValorEmReal + "em doláres seria" + ValorEmEuro);

fim
--------------------------------
'''

ValorEmEuro = float(input("Digite o valor em Euro: "))

ValorEmEuro = ValorEmEuro / 0.20

print(f"{ValorEmReal} Euros em Reais seria {ValorEmEuro}")