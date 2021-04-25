from ContaBancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def __init__(self, id, nome):
        ContaBancaria.__init__(self, id, nome)
        self.__saldo = 0

    def cadastrar(self):
        print("➯ Conta Poupança cadastrada com sucesso")

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, novo_id):
        pass

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        if novo_nome != "":
            print('➯ Alteracao de nome: {} ➯ {}'.format(self._nome, novo_nome))
            self._nome = novo_nome

        else:
            print("➯ Valor nao permitido")

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def depositar(self, saldo_soma):
        if saldo_soma >= 0:
            self.__saldo += saldo_soma
            print('➯ Saldo alterado com sucesso')
        else:
            print("➯ Valor nao permitido")



Cp1 = ContaPoupanca('CP1', 'FatOne')
Cp1.depositar = 20.0
print("➯",Cp1.saldo,"\n")

print("➯",Cp1.nome)
Cp1.nome = 'Richier than ever'
print("➯",Cp1.nome)
Cp1.depositar = 100000000000000000.8765432
print("➯",Cp1.saldo,"\n")