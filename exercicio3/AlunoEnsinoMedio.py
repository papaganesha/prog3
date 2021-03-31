from Aluno import *


class AlunoEnsinoMedio(Aluno):
    def __init__(self, codigo, nome, matricula, ano):
        self.aluno = Aluno.__init__(self, codigo, nome, matricula)
        self.ano = ano

    def imprimir_Aluno(self):
        print("\n○ Aluno Medio\n        Codigo: {}\n        Nome: {}\n        Matricula: {}\n        Ano: {}º".format(self.codigo, self.nome, self.matricula, self.ano))






