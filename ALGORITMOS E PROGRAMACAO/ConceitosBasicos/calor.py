'''
Desenvolva um algoritmo que recebe uma temperatura em graus Celsius (C), 
calcula e mostra a temperatura convertida em graus Fahrenheit (F). Fórmula de conversão: F = (9.C + 160) / 5.

Algoritmo ConversaoGraus
    Declarar
        C inteiro;
    
  //Entrada de dados e o processamento dos dados
  escrever("Digite uma temperatura em graus Celsius: "); //essa mensagem aparece na tela do usuário
  ler(C); // o que o usuário digitar, é armazenado na variável C 

  //Processamento de dados
  F = (9 * C + 160) / 5.

  //Saída dos resultados
  escrever ("A temperatura em Celsius convertida em graus Fahrenheit:  " + F);

fim
'''
import decimal

C = decimal.Decimal(input("Digite uma temperatura em graus Celsius: "))

F = (9 * C + 160) / 5

print(f"A temperatura em Celsius convertida em graus Fahrenheit: {F}")
