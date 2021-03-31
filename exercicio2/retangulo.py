


class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura
        #self.imprimirRetangulo()

    def get_area(self):
        area = self.altura * self.largura
        return area

    def get_perimetro(self):
        perimetro = (self.altura*2)+(self.largura*2)
        return perimetro

    def imprimirRetangulo(self):
        print("Altura: {}, Largura: {}".format(self.altura, self.largura))


    def __repr__(self):
        return "altura {}, largura {}".format(self.altura, self.largura)





