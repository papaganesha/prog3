from Veiculo import *


class Automovel(Veiculo):
    def __init__(self, marca, qtdRodas, modelo,potencia):
        Veiculo.__init__(self, marca, qtdRodas, modelo)
        self.potencia = str(potencia)+" cavalos"


    def print_info(self):
        print('''
Automovel -- Marca: {}
             Qtd_Rodas: {}
             Modelo: {}
             Velocidade: {}
             Potencia_Motor: {}'''.format(self.marca, self.qtdRodas, self.modelo, self.velocidade, self.potencia))



