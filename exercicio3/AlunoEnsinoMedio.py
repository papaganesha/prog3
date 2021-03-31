from Aluno import *


class AlunoEnsinoMedio(Aluno):
    def __init__(self, codigo, nome, matricula, ano):
        self.aluno = Aluno.__init__(self, codigo, nome, matricula)
        self.ano = ano
        self.imprimir_Aluno_Medio()

    def imprimir_Aluno_Medio(self):
        print("○ Aluno Medio\n        Codigo: {}\n        Nome: {}\n        Matricula: {}\n        Ano: {}º".format(self.codigo, self.nome, self.matricula, self.ano))






