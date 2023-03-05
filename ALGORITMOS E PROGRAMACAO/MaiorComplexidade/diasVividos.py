import decimal

#entrada de dados
DN = decimal.Decimal(input("Digite o seu dia de nascimento: "))
MN = decimal.Decimal(input("Digite o seu mês de nascimento: "))
AN = decimal.Decimal(input("Digite o seu ano de nascimento: "))
DA = decimal.Decimal(input("Digite o seu dia de atual: "))
MA = decimal.Decimal(input("Digite o seu mês de atual: "))
AA = decimal.Decimal(input("Digite o seu ano de atual: "))

#processamento dos dados
DN = DN + MN*30 + AN*365;
DA = DA + MA*30 + AA*365;
DN = DA - DN;
AA = DN // 365; # quantos anos eu já vivi
MA = (DN % 365) // 30; # quantos meses eu já vivi
DA = (DN % 365) % 30; # quantos dias eu já vivi

#saída dos resultados
print (f"Você já viveu {AA} anos {MA} meses e {DA} dias")
