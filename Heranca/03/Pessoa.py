

class Pessoa():
    def __init__(self, nome):
        self.nome = nome


    def get_Pessoas(self):
        print('Pessoa\n     Nome: {}'.format(self.nome))


class PessoaFisica(Pessoa):
    def __init__(self, nome, cpf):
        Pessoa.__init__(self, nome)
        self.cpf = cpf

    def get_PessoasFisicas(self):
        print('\nPessoa Fisica\n     Nome: {}\n     Cpf: {}'.format(self.nome, self.cpf))



class PessoaJuridica(Pessoa):
    def __init__(self, nome, nomeFantasia, CNPJ, razaoSocial):
        Pessoa.__init__(self, nome)
        self.nomeFantasia = nomeFantasia
        self.CNPJ = CNPJ
        self.razaoSocial = razaoSocial


    def get_PessoasJuridicas(self):
        print('\nPessoa Juridica\n     Nome: {}\n     NomeFantasia: {}\n     CNPJ: {}\n     RazaoSocial: {}'.format(self.nome, self.nomeFantasia, self.CNPJ, self.razaoSocial))


pf = PessoaFisica("Maicon", "037.665.123-00")
pf.get_PessoasFisicas()


pj = PessoaJuridica("Marlon", "Maicon Moveis", "00032343233234", "MaiconMoveisLimitada")
pj.get_PessoasJuridicas()