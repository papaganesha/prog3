from Pessoa import *

class Funcionario(PessoaFisica):
    def __init__(self, nome, cpf, matricula, salario_base, carga_horaria, qtd_horas):
        PessoaFisica.__init__(self, nome, cpf)
        self.matricula = matricula
        self.salario_base = float(salario_base)
        self.carga_horaria = carga_horaria
        self.qtd_horas = qtd_horas



    def calculaBonus(self):
        return 0.0


    def calcula_SalarioBruto(self):
        calculo = self.salario_base * ((self.qtd_horas/self.carga_horaria)+ self.calculaBonus())
        print("     Salario Bruto de {}: R${}".format(self.nome, calculo))



funcionarinho = Funcionario("Jairo", "034.007.130-99","004", 2500, 30, 50)
funcionarinho.get_PessoasFisicas()
funcionarinho.calcula_SalarioBruto()