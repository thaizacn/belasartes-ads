import impressora

#Interações com a classe "impressora.py"
minha_impressora = impressora.Impressora()

while True:
    #Deixando o usuário decidir o que será feito
    print("===== MENU DE IMPRESSORA =====")
    print("1 - Realizar uma impressão")
    print("2 - Verificar nível do cartucho")
    print("3 - Recarregar cartucho")
    print("4 - Encerrar impressão")
    decisao = input("Escolha uma opção: ")

    if decisao == "1":
        minha_impressora.imprimir(input("Digite o texto que será impresso: "))
        print()
    elif decisao == "2":
        minha_impressora.nivel_do_cartucho()
        print()
    elif decisao == "3":
        minha_impressora.recarregar_cartucho()
        print()
    elif decisao == "4":
        break
    else:
        print("Opção inválida. Tente novamente.")
        print()




