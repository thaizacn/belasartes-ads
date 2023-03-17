class Impressora:
    def __init__(self):
        self.nivel_cartucho = 100

    def imprimir(self, texto):
        if self.nivel_cartucho <= 0:
            print("A tinta do cartucho acabou!")
        else:
            print("Imprimindo:", texto)
            self.nivel_cartucho -= 20
            return

    def nivel_do_cartucho(self):
        print("Nível do cartucho:", self.nivel_cartucho)

    def recarregar_cartucho(self):
        self.nivel_cartucho = 100


