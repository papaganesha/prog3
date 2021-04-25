from Aula07_CAbstratas.model.Animal import Animal

class Bovino(Animal):
    def __init__(self, idade):
        if idade > 0:
            self._idade = idade
        else:
            self._idade = 0

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, newIdade):
        if newIdade >= 0:
            self._idade = newIdade
            print('➯ Idade alterada com sucesso')
        else:
            print("➯ Valor nao permitido")




    def cadastrar(self):
        print("➯ Bovino cadastrado com sucesso")


