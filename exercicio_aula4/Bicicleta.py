from Veiculo import *

class Bicicleta(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, numMarchas, bagageiro = False):
        Veiculo.__init__(self, marca, qtdRodas, modelo)
        self.velocidade = 0
        self.numMarchas = numMarchas
        self.bagageiro = bagageiro



    def print_info(self):
        print('''
Veiculo -- Marca: {}
           Qtd_Rodas: {}
           Modelo: {}
           Velocidade: {}
           Num_Marchas: {}
           Bagageiro: {}'''.format(self.marca, self.qtdRodas, self.modelo, self.velocidade, self.numMarchas, self.bagageiro))


