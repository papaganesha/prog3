from Aula06.Pessoas.model.Pessoa import Pessoa

class Juridica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone, cnpj, inscricaoEstadual,  quantidadeFuncionarios):
        Pessoa.__init__(self, codigo, nome, endereco, telefone)
        self.__cnpj = cnpj
        self.__inscricaoEstadual = inscricaoEstadual
        self.quantidadeFuncionarios = quantidadeFuncionarios

    def imprime_CNPJ(self):
        print("CPF: {}".format(self.__cnpj))

    def __emitirNotaFiscal(self):
        print('Artefato Nota Fiscal')

