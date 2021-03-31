

class Aluno:
    def __init__(self, codigo, nome, matricula):
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula

    def imprimir_Aluno(self):
        print("○ Aluno\n        Codigo: {}\n        Nome: {}\n        Matricula: {}".format(self.codigo, self.nome, self.matricula))



