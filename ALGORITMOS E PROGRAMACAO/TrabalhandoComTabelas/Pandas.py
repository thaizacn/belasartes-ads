import pandas as pd

Clientes = pd.read_csv("Clientes.csv") 
Pedidos = pd.read_csv("Pedidos.csv")

N = 0

for Contador in Clientes:
    if (N == 0):
        N =+ 1
        continue

    ClienteId =  Clientes['Id']
    ClienteNome =  Clientes['Nome']
    ClienteTelefone =  Clientes['Telefone']

    N2 = 0
    for Contador2 in Pedidos:
        if (N2 == 0):
            N2 =+ 1
            continue

        PedidoId = Pedidos['Id']
        PedidoIdCliente = Pedidos['Id_Cliente']
        PedidoDescricao = Pedidos['Descricao']
        PedidoQuantidade = Pedidos['Quantidade']

        if PedidoIdCliente.equals(ClienteId):
            print("Nome: " + ClienteNome)
            print("Telefone: " + ClienteTelefone)
            print("Produto: " + PedidoDescricao)
            print("Quantidade: " + PedidoQuantidade)
            print("----------------------------------")

print("Fim")