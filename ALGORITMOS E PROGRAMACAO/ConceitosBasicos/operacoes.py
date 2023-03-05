'''
--------------------------------
Desenvolva um algoritmo que realiza todas as operações matemáticas: adição, subtração, multiplicação e divisão

Algoritmo OperacoesMatematicas
inicio
  Declarar
    Valor1 inteiro;
    Valor2 inteiro;

  //Entrada de dados e o processamento dos dados
  escrever("Digite o primeiro valor: "); 
  ler(Valor1); 
  escrever("Digite o segundo valor: "); 
  ler(Valor2); 

  //Processamento de dados
  Resultado = Valor1 + Valor2; //e repetir para as demais operações dando "print" no resultado na sequência

  //Saída dos resultados
  escrever ("A adição de {Valor1} com {Valor2} resulta em {Resultado}.");

fim
--------------------------------
'''

import decimal

Valor1 = decimal.Decimal(input("Digite o primeiro valor: "))
Valor2 = decimal.Decimal(input("Digite o segundo valor: "))

Resultado = Valor1 + Valor2;
print (f"\nA adição de {Valor1} com {Valor2} resulta em {Resultado}.")

Resultado = Valor1 - Valor2;
print (f"A subtração de {Valor1} com {Valor2} resulta em {Resultado}.")

Resultado = Valor1 * Valor2;
print (f"A multiplicação de {Valor1} com {Valor2} resulta em {Resultado}.")

Resultado = Valor1 / Valor2;
print (f"A divisão de {Valor1} com {Valor2} resulta em {Resultado}.")

'''
Desenvolva um algoritmo que recebe um valor numérico_real, calcula e mostra o quadrado deste número.

Algoritmo CalculaQuadrado
inicio
  Declarar
    Valor1 inteiro;

  //Entrada de dados e o processamento dos dados
  escrever("Digite um valor para calcularmos o quadrado: "); 
  ler(Valor1); 

  //Processamento de dados
  Resultado = Valor1 ** 2

  //Saída dos resultados
  escrever ("O quadrado de" + Valor1 + "é igual a: " + Resultado);

fim

'''

Valor1 = float(input("\nDigite um valor para calcularmos o quadrado: "))

Resultado = Valor1 ** 2

print(f"O quadrado de {Valor1}, é igual a: {Resultado}")

'''
Desenvolva um algoritmo que recebe dois valores numérico_inteiro, calcula e mostra a soma do quadrado desses dois números.

Algoritmo SomaDoQuadrado
inicio
  Declarar
    Valor1 inteiro;
    Valor2 inteiro;

  //Entrada de dados e o processamento dos dados
  escrever("Digite um valor do primeiro quadrado: "); 
  ler(Valor1); 
  escrever("Digite um valor do segundo quadrado: "); 
  ler(Valor2); 

  //Processamento de dados
  Quadrado1 = Valor1 ** 2
  Quadrado2 = Valor2 ** 2
  SomaQuadrados = Quadrado1 + Quadrado2

  //Saída dos resultados
  escrever ("A soma do quadrado dos valores é de: " + SomaQuadrados);

fim

'''

Valor1 = float(input("\nDigite um valor do primeiro quadrado: "))
Valor2 = float(input("Digite um valor do segundo quadrado: "))

Quadrado1 = Valor1 ** 2
Quadrado2 = Valor2 ** 2
SomaQuadrados = Quadrado1 + Quadrado2

print(f"A soma do quadrado dos valores é de: {SomaQuadrados}")