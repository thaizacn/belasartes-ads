class Impressora:
    def __init__(self):
        self.nivel_cartucho = 100
        
    def entrada_com_texto(self):
        self.texto = input("Digite o texto a ser impresso: ")
        
    def imprimir(self):
        if self.nivel_cartucho >= 20:
            print("Imprimindo...")
            self.nivel_cartucho -= 20
        else:
            print("A tinta do cartucho acabou!")
        
    def verificar_nivel_cartucho(self):
        print("Nível de cartucho: {}%".format(self.nivel_cartucho))
        
    def recarregar_cartucho(self):
        self.nivel_cartucho = 100
        print("Cartucho recarregado!")
