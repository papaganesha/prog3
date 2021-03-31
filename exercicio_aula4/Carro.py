from Automovel import *





class Carro(Automovel):
    def __init__(self, marca, qtdRodas, modelo,  potencia, qtdPortas):
        Automovel.__init__(self, marca, qtdRodas, modelo, potencia)
        self.qtdPortas = qtdPortas

    def print_info(self):
        print('''
Carro -- Marca: {}
         Modelo: {}
         Qtd_Rodas: {}
         Qtd_Portas: {}
         Velocidade: {}
         Potencia_Motor: {}'''.format(self.marca, self.modelo, self.qtdRodas,self.qtdPortas, self.velocidade, self.potencia))



