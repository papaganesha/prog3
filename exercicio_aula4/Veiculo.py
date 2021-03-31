


class Veiculo:
    def __init__(self, marca, qtdRodas, modelo):
        self.marca = str(marca)
        self.qtdRodas = int(qtdRodas)
        self.modelo = str(modelo)
        self.velocidade = velocidade = 0

    def print_info(self):
        print('''
Veiculo -- Marca: {}
           Qtd_Rodas: {}
           Modelo: {}
           Velocidade: {}'''.format(self.marca, self.qtdRodas, self.modelo, self.velocidade))

    def acelerar(self, val):
        self.velocidade = self.velocidade + val


    def frear(self, val):
        self.velocidade = self.velocidade - val

