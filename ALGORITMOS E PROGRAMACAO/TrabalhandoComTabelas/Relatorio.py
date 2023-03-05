import csv

Clientes = open("Clientes.csv","r")
Pedidos = open("Pedidos.csv","r")

N = 0

for Contador in list(Clientes):
    
    if (N == 0):
        N =+ 1
        continue

    ArrayClientes = Contador.split(",")

    ClienteId =  ArrayClientes[0]
    ClienteNome =  ArrayClientes[1]
    ClienteTelefone =  ArrayClientes[2]

    Pedidos.seek(0)

    N2 = 0
    for Contador2 in list(Pedidos):
        if (N2 == 0):
            N2 =+ 1
            continue

        ArrayPedidos = Contador2.split(",")

        PedidoId = ArrayPedidos[0]
        PedidoIdCliente = ArrayPedidos[1]
        PedidoDescricao = ArrayPedidos[2]
        PedidoQuantidade = ArrayPedidos[3]

        if PedidoIdCliente == ClienteId:
            print("Nome: " + ClienteNome)
            print("Telefone: " + ClienteTelefone)
            print("Produto: " + PedidoDescricao)
            print("Quantidade: " + PedidoQuantidade)
            print("----------------------------------")

print("Fim")