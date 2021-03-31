from Aluno import *


class Aluno_Graduacao(Aluno):
    def __init__(self, codigo, nome, matricula, semestre):
        Aluno.__init__(self, codigo, nome, matricula)
        self.semestre = semestre

    def imprimir_Aluno(self):
        print("\n○ Aluno Graduacao\n        Codigo: {}\n        Nome: {}\n        Matricula: {}\n        Semestre: {}º".format(self.codigo, self.nome, self.matricula, self.semestre))



