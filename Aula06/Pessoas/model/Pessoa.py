class Pessoa:
    def __init__(self, codigo, nome, endereco, telefone):
        self.__codigo = codigo
        self.nome = nome
        self._endereco = endereco
        self.__telefone = telefone
        self.verTelefone = self.__imprime_Telefone()
    def imprime_nome(self):
        print('Nome: {}'.format(self.nome))

    def __imprime_Telefone(self):
        return 'Telefone: {}'.format(self.__telefone)

