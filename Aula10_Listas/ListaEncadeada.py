# Classe nodo/nó

class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


# Classe Lista Encadeada
class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def adicionar(self, valor):
        if self.inicio:
            aux = self.inicio

            while (aux.proximo):
                aux = aux.proximo

            aux.proximo = No(valor)
        else:
            self.inicio = No(valor)

        print('------------------- Inserindo itens na Lista Encadeada --------------------')
        print("➥ {} inserido na Lista Encadeada".format(valor))
        print('---------------------------------------------------------------------------\n')
        self.tamanho += 1

    def imprimir(self):
        if self.inicio == None:
            print('------------------- Imprimindo itens da Lista Encadeada -------------------')
            print("➥ Lista Vazia")
            print('---------------------------------------------------------------------------\n')

        else:
            aux = self.inicio
            count = 0
            print('------------------- Imprimindo itens da Lista Encadeada -------------------')
            while (aux):
                print("⊡",count, ":", aux.dado)
                aux = aux.proximo
                count += 1
            print('---------------------------------------------------------------------------\n')

    def excluir(self, valor):
        print('------------------- Excluindo itens da Lista Encadeada -------------------')
        if self.tamanho == 0:
            print('------------------- Excluindo itens da Lista Encadeada -------------------')
            print("➥ Lista Vazia")
            print('---------------------------------------------------------------------------\n')

        elif self.tamanho == 1:
            if self.inicio.dado == valor:
                self.inicio = None
                self.tamanho -= 1
            else:
                print("➥ Valor nao encontrado")

        else:
            tamAnterior = self.tamanho
            if self.inicio.dado == valor:
                self.inicio = self.inicio.proximo
                self.tamanho -= 1
            else:
                anterior = self.inicio
                aux = self.inicio.proximo
                while (aux):
                    if (aux.dado == valor):
                        anterior.proximo = aux.proximo
                        self.tamanho -= 1

                    anterior = aux
                    aux = aux.proximo
            if tamAnterior == self.tamanho:
                print("➥ Valor nao encontrado")
            print('➥ {} excluido com sucesso da Lista Encadeada'.format(valor))
            print('---------------------------------------------------------------------------\n')

            self.imprimir()


# Executando
lenc = ListaEncadeada()
lenc.imprimir()
lenc.adicionar('jorge ruiz')
lenc.imprimir()
lenc.adicionar('jorge marinara')
lenc.imprimir()
lenc.adicionar(10.00)
lenc.imprimir()
lenc.excluir(10.00)
