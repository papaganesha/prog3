from Automovel import *


class Moto(Automovel):
    def __init__(self, marca, qtdRodas, modelo,  potencia, partidaEletrica=False):
        Automovel.__init__(self, marca, qtdRodas, modelo, potencia)
        self.partidaEletrica = partidaEletrica

    def print_info(self):
        print('''
Moto.py --  Marca: {}
         Modelo: {}
         Qtd_Rodas: {}
         Velocidade: {}
         Partida_Eletrica: {}
         Potencia_Motor: {}'''.format(self.marca, self.modelo, self.qtdRodas, self.velocidade,self.partidaEletrica , self.potencia))



v4 = Moto("Cg", 2, "125", 200, )
v4.print_info()
v4.acelerar(200)
v4.frear(120)
v4.print_info()