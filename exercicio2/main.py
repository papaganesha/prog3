from retangulo import *

if __name__ == '__main__':
    retangulos = []
    def insert_retangulo():
        print("\n○ Inserindo novo retangulo")
        try:
            altura = int(input("○ Altura: "))
            largura = int(input("○ Largura: "))
            retangulo_Insert = Retangulo(altura, largura)
            retangulos.append(retangulo_Insert)
            input('○ Retangulo adicionado [ENTER]')
        except Exception as e:
            input("○ {}, [ENTER]".format(e))
            insert_retangulo()

    def print_area_perimetro(retangulos):
        print("○ Imprimindo retangulo(s)")
        cont = 0
        for retangulo in retangulos:
            print("○ Info Retangulo{}: {}, area: {}, perimetro: {}".format(cont + 1, retangulo.__repr__(),
                                                                           retangulo.get_area(),
                                                                           retangulo.get_perimetro()))
            cont += 1

    def print_atributos_retangulos(retangulos):
        print("○ Imprimindo retangulo(s)")
        cont = 0
        for retangulo in retangulos:
            retangulo.imprimirRetangulo()




retangulo1 = Retangulo(5, 2)
retangulo2 = Retangulo(10, 4)
retangulo3 = Retangulo(20, 4)
retangulo4 = Retangulo(5, 4)
retangulos.append(retangulo1)
retangulos.append(retangulo2)
retangulos.append(retangulo3)
retangulos.append(retangulo4)
insert_retangulo()

#print_atributos_retangulos(retangulos)
print_area_perimetro(retangulos)




