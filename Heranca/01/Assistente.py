from Funcionario import *


class Assistente(Funcionario):
    def __init__(self, cod_func, nome, salario, matricula):
        Funcionario.__init__(self, cod_func, nome, salario)
        self.matricula = matricula

    def get_Assistente(self):
        print("Assistente:\n       cod_func: {}\n       nome: {}\n       salario: R${}\n       matricula: {}".format(self.cod_func, self.nome, self.salario, self.matricula))


