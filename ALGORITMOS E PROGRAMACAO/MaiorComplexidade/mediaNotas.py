'''
------------------------------------------
Desenvolva um algoritmo que recebe os valores referentes a quatro notas bimestrais de um aluno, calcula a média deste aluno 
e mostra a mensagem de aprovação (média >= 5) ou reprovação (média < 5) do aluno, juntamente com a média calculada.

Algoritmo NotasBimestrais
    Declarar
        //escolhi float pois a nota pode ter casas decimais
        QuatroNotas float;
    
  //Entrada de dados e o processamento dos dados
  escrever("Digite suas quatro notas bimestrais separados por vírgula: "); 
  ler(QuatroNotas); 

  //Processamento de dados
  Um, Dois, Tres, Quatro = QuatroNotas.split(",")
  Um, Dois, Tres, Quatro = float(Um), float(Dois), float(Tres), float(Quatro)

  Media = (Um + Dois + Tres + Quatro) / Quatro

  //Saída dos resultados
  if (Media >= 5)
  print("Parabéns você foi aprovado")

  else
  print("Infelizmente você foi reprovado, estude mais um pouco!")

fim
--------------------------------------------
'''

QuatroNotas = input("Digite suas quatro notas bimestrais separados por vírgula: ")

Um, Dois, Tres, Quatro = QuatroNotas.split(",")
Um, Dois, Tres, Quatro = float(Um), float(Dois), float(Tres), float(Quatro)

Media = (Um + Dois + Tres + Quatro) / 4

if (Media >= 5):
  print(f"Parabéns você foi aprovado, sua média foi {Media}")
else:
  print(f"Infelizmente você foi reprovado, estude mais um pouco, sua média foi {Media}")