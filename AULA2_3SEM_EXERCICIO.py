# Construa um algoritmo para implementar a classe Retangulo que possui os atributos: altura e largura.
# A classe deve ter os seguintes métodos:
# ○ Metodo construtor
# ○ Metodo que calcula a área do retângulo(altura * largura) e retorna o resultado
# ○ Metodo que imprime os valores dos atributos da classe



class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def get_area(self):
        area = self.altura * self.largura
        return area

    def __repr__(self):
        return "altura {}, largura {}".format(self.altura, self.largura)


retangulo1 = Retangulo(5,2)
retangulo2 = Retangulo(10, 4)
retangulo3 = Retangulo(20, 4)

retangulos = [retangulo1, retangulo2, retangulo3]

cont = 0
for retangulo in retangulos:
    print("Info Retangulo{}: {}, area: {}".format(cont+1, retangulo.__repr__(), retangulo.get_area()))
    cont += 1