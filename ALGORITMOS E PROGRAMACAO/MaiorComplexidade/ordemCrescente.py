'''
--------------------------------------------
Desenvolva um algoritmo que recebe três valores numérico_real e mostre-os em ordem crescente. 
Utilizar a estrutura de decisão encadeada.

Algoritmo OrdemCrescente
    Declarar
        TresValores reais;
    
  //Entrada de dados e o processamento dos dados
  escrever("Digite três valores separados por vírgula: "); 
  ler(TresValores); 

  //Processamento de dados
  Um, Dois, Tres = TresValores.split(",")
  Um, Dois, Tres, Quatro = float(Um), float(Dois), float(Tres)

  se(Um <= Dois) e (Um <= Tres):
    se(Dois <= Tres)
        escrever("Em ordem crescente ficará: {Um}, {Dois}, {Tres}")
    senao:
        escrever("Em ordem crescente ficará: {Um}, {Tres} e {Dois}")

  se(Dois <= Um) e (Dois <= Tres):
    se(Um <= Tres):
        escreve("Em ordem crescente ficará: {Dois}, {Um}, {Tres}")
    senao:
        escreve("Em ordem crescente ficará: {Dois}, {Tres}, {Um}")

se(Tres <= Um) e (Tres <= Dois):
    se(Um <= Dois):
        escreve("Em ordem crescente ficará: {Tres}, {Um}, {Dois}")
    senao:
        escreve("Em ordem crescente ficará: {Tres}, {Dois}, {Um}")
  
  //Saída dos resultados
  A saidas serao escritas conforme o processamento

fim
-----------------------------------------------
'''

TresValores = input("Digite suas quatro notas bimestrais separados por vírgula: ")

Um, Dois, Tres = TresValores.split(",")
Um, Dois, Tres = float(Um), float(Dois), float(Tres)

if(Um <= Dois) and (Um <= Tres):
    if(Dois <= Tres):
        print(f"Em ordem crescente ficará: {Um}, {Dois}, {Tres}")
    else:
        print(f"Em ordem crescente ficará: {Um}, {Tres}, {Dois}")

if(Dois <= Um) and (Dois <= Tres):
    if(Um <= Tres):
        print(f"Em ordem crescente ficará: {Dois}, {Um}, {Tres}")
    else:
        print(f"Em ordem crescente ficará: {Dois}, {Tres}, {Um}")

if(Tres <= Um) and (Tres <= Dois):
    if(Um <= Dois):
        print(f"Em ordem crescente ficará: {Tres}, {Um}, {Dois}")
    else:
        print(f"Em ordem crescente ficará: {Tres}, {Dois}, {Um}")

