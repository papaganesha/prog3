from Funcionario import *


class Gerente(Funcionario):
    def __init__(self, cod_func, nome, salario, departamento):
        Funcionario.__init__(self, cod_func, nome, salario)
        self.departamento = departamento

    def get_Gerente(self):
        print("Gerente:\n       cod_func: {}\n       nome: {}\n       salario: R${}\n       departamento: {}".format(self.cod_func, self.nome, self.salario, self.departamento))


