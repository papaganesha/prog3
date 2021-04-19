

class Funcionario:
    def __init__(self, cod_func, nome, salario):
        self.cod_func = cod_func
        self.nome = nome
        self.salario = float(salario)


    def get_Funcionario(self):
        print("Funcionario:\n       cod_func: {}\n       nome: {}\n       salario: R${}".format(self.cod_func, self.nome, self.salario))


