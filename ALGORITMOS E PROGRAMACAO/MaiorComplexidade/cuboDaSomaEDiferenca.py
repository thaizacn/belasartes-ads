'''
-----------------------------------------------
Desenvolva um algoritmo que recebe três valores numérico_inteiro, calcula e mostra o cubo da soma desses três números.

Algoritmo CuboDaSoma
inicio
    Declarar
        TresValores inteiro;
    
  //Entrada de dados e o processamento dos dados
  escrever("Digite três valores inteiros separados por vírgula: "); //essa mensagem aparece na tela do usuário
  ler(TresValores); // o que o usuário digitar, é armazenado na variável NumeroReal 

  //Processamento de dados
  Se(A e B e C != 0)
  Equacao = A + B + C
  SomaCubo = Equacao ** 3

  //Saída dos resultados
  escrever ("O cubo da soma dos números é: " + Resultado);

fim
-----------------------------------------------
'''

TresValores = input("Digite três valores inteiros separados por vírgula: ")

A, B, C = TresValores.split(",")
A, B, C = int(A), int(B), int(C)

Equacao = A + B + C
SomaCubo = Equacao ** 3

print(f"O cubo da soma dos números é: {SomaCubo}")

'''
-------------------------------------------
Desenvolva um algoritmo que recebe três valores numérico_real, calcula e mostra a diferença do cubo desses três números.

Algoritmo CuboDaDiferença
inicio
    Declarar
        TresValores inteiro;
    
  //Entrada de dados e o processamento dos dados
  escrever("Digite três valores inteiros separados por vírgula: "); //essa mensagem aparece na tela do usuário
  ler(TresValores); // o que o usuário digitar, é armazenado na variável NumeroReal 

  //Processamento de dados
  Se(A e B != 0)


  //Saída dos resultados
  escrever ("O cubo da soma dos números é: " + Resultado);

fim
-----------------------------------------------
'''

TresValores = input("Digite três valores inteiros separados por vírgula: ")

A, B, C = TresValores.split(",")
A, B, C = int(A), int(B), int(C)

Equacao = A - B - C
DiferencaCubo = Equacao ** 3

print(f'O cubo da soma dos números é: {DiferencaCubo}')