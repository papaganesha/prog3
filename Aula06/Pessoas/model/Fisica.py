from Aula06.Pessoas.model.Pessoa import Pessoa

class Fisica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone, cpf, idade, peso, altura):
        Pessoa.__init__(self, codigo, nome, endereco, telefone)
        self.__cpf = cpf
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def imprime_CPF(self):
        print("CPF: {}".format(self.__cpf))

    def __calcula_IMC(self):
        formula = self.peso / (self.altura**2)
        return formula



