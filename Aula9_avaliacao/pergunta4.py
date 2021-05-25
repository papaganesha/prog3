#Construir código necessário em Python para implementar o seguinte projeto:
#Uma classe abstrata chamada de Computador que contém os atributos/propriedades modelo, cor e preço.
# Esta classe também possui um método getInformacoes() que retorna todos os valores dos atributos.
# Esta classe também possui um método abstrato cadastrar().
#O projeto tambem deve possuir as classes Desktop e Notebook que herdam da classe Computador.
#A classe Desktop possui o atributo/propriedade fracamente privado potenciaDaFonte.
# Esta classe reimplementa o método getInformacoes() herdado de computador.
#A classe Notebook possui o atributo/propriedade fortemente privado tempoDeBateria.
# Esta classe reimplementa o método getInformacoes() herdado de computador.

from abc import ABCMeta, abstractmethod


class Computador(metaclass=ABCMeta):

    @property
    def getInformacoes(self):
        pass

    @property
    def cor(self):
        pass

    @cor.setter
    @abstractmethod
    def cor(self, newCor):
        pass


    @property
    def preco(self):
        pass

    @preco.setter
    @abstractmethod
    def preco(self, newPreco):
        pass

    @abstractmethod
    def cadastrar(self):
        pass



class Desktop(Computador):
    def __init__(self, cor, preco, potenciaDaFonte):
        self.__cor = cor
        self.__preco = preco
        self._potenciaDaFonte = potenciaDaFonte

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, newCor):
        if newCor != "":
            self.__cor = newCor
            print('➯ Cor alterada com sucesso para {}'.format(newCor))
        else:
            print("➯ Valor nao permitido")

    @property
    def getInformacoes(self):
        return [self.__cor, self.__preco, self._potenciaDaFonte]

    @property
    def potenciaDaFonte(self):
        return self._potenciaDaFonte

    @potenciaDaFonte.setter
    def potenciaDaFonte(self, newPotencia):
        if newPotencia != "" and newPotencia != None:
            self._potenciaDaFonte = newPotencia
            print('➯ Potencia da fonte alterado com sucessa para {}'.format(newPotencia))
        else:
            print("➯ Valor nao permitido")


    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, newPreco):
        if newPreco != 0.0 and newPreco != None:
            self.__preco = newPreco
            print('➯ Preco alterado com sucesso para R${}'.format(newPreco))
        else:
            print("➯ Valor nao permitido")

    @property
    def cadastrar(self):
        print('Computador DESKTOP foi criado\nCor: {}\nPreço: {}\nPotenciaFonte: {}'.format(self.__cor, self.__preco, self._potenciaDaFonte))




class Notebook(Computador):
    def __init__(self, cor, preco, tempoBateria):
        self.__cor = cor
        self.__preco = preco
        self.__tempoBateria = tempoBateria

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, newCor):
        if newCor != "":
            self.__cor = newCor
            print('➯ Cor alterada com sucesso para {}'.format(newCor))
        else:
            print("➯ Valor nao permitido")

    @property
    def getInformacoes(self):
        return [self.__cor, self.__preco, self.__tempoBateria]

    @property
    def tempoBateria(self):
        return self.__tempoBateria

    @tempoBateria.setter
    def tempoBateria(self, newTempoBateria):
        if newTempoBateria != 0.0 and newTempoBateria != None:
            self.__tempoBateria = newTempoBateria
            print('➯ Tempo de bateria alterado com sucesso para {}'.format(newTempoBateria))
        else:
            print("➯ Valor nao permitido")


    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, newPreco):
        if newPreco != 0.0 and newPreco != None:
            self.__preco = newPreco
            print('➯ Preco alterado com sucesso para R${}'.format(newPreco))
        else:
            print("➯ Valor nao permitido")

    @property
    def cadastrar(self):
        print('Computador NOTEBOOK foi criado\nCor: {}\nPreço: {}\nTempoBateria(valorficticio em Horas): {}'.format(self.__cor, self.__preco, self.__tempoBateria))






desktop = Desktop('preto', 2000.00, '220')
desktop.cadastrar
print(desktop.getInformacoes)
print(desktop.cor)
print(desktop.preco)
print(desktop.potenciaDaFonte)
desktop.cor = 'azul'
print(desktop.getInformacoes)
desktop.preco = 3000.00
print(desktop.getInformacoes)
desktop.potenciaDaFonte = 'bivolt'
print(desktop.getInformacoes)


print('\n\n\n\n-----------------------------------------------\n\n\n\n')


notebook = Notebook('marrom', 8000.00, 4.5)
notebook.cadastrar
print(notebook.getInformacoes)
print(notebook.cor)
print(notebook.preco)
print(notebook.tempoBateria)
notebook.cor = 'prata'
print(notebook.getInformacoes)
notebook.preco = 7500.00
print(notebook.getInformacoes)
notebook.tempoBateria = 5.5
print(notebook.getInformacoes)
