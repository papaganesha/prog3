import random
#print(random.randint(1, 100))
from copy import copy

from pandas.plotting import table


class Apartamento:
    def __init__(self, id, numero, torre = None):
        self._id = id
        self._numero = numero
        self._torre = torre
        self.vaga = 0

    def __iter__(self):
        return self


    def alterarVaga(self, valor):
        valorInt = int(valor)
        self.vaga = valorInt


    def cadastrarOnQueue(self):
        filaBlocoA.enqueue(self)

    def imprimirQueue(self):
        filaBlocoA.showQueue()


    def imprimirSelf(self):
        id = self._id
        numero = self._numero
        torre = self._torre
        vaga = self.vaga
        print("ID:{} ---- NUMERO:{} ---- TORRE:{} ---- VAGA:{}".format(id, numero, torre, vaga))







def populandoVagas(param):
        if param == 10:
            vagasShuffle = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            random.shuffle(vagasShuffle)
            return vagasShuffle
        elif param == 15:
                vagasShuffle = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
                random.shuffle(vagasShuffle)
                return vagasShuffle
        else:
            vagasShuffle = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            random.shuffle(vagasShuffle)
            return vagasShuffle



class Queue:
    def __init__(self):
        self.items = []
        self._nroVagas = 10
        self._vagasDisponiveis = populandoVagas(self._nroVagas)


    def __iter__(self):
        '''Pegar indice aleatorio dentro do tamanho atual de VagasDisponiveis, escolhe ele na lista e coloca para alterar
         a vaga do Apartamento X(primeiro da fila no momento, sabendo do comportamento da Fila tambem setando para
         excluir o primeiro da fila e excluir a vaga que foi retirada das VagasDisponiveis'''
        print("\nAtribuindo vagas automaticamente")
        if (self.vagasEmpty() == False):
            try:
                for item in self.items:
                    vagaNova = self._vagasDisponiveis[0]
                    print("APP N: {} ---- VAGA: {} -> {} ".format(item._numero, item.vaga, vagaNova))
                    item.alterarVaga(vagaNova)
                    self._vagasDisponiveis.pop(0)
                self.dequeue()

            except:
                 print("Acabaram as vagas")
        else:
            print("Acabaram as vagas")



    def vagasSize(self):
        return len(self._vagasDisponiveis)

    def vagasEmpty(self):
        return self._vagasDisponiveis == []

    def isEmpty(self):
        return self.items == []

    def showQueue(self):
        print("\nFila de Apartamentos esperando vaga")
        i = 1
        for itens in self.items:
            print("{} --  APP N: {}".format(i, itens._numero))
            i +=1

    def enqueue(self, item):
        check = self.isEmpty()
        if  check == True:
            self.items.insert(0,item)
        else:
            self.items.append(item)


    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)





class Torre:
    def __init__(self, id:int, nome:str, endereco:str):
        self._id = id
        self._nome = nome
        self._endereco = endereco
        self._Apartamentos : list = []

    def vagasSize(self):
        return len(self.vagasDisponiveis)

    def vagasEmpty(self):
        return self.vagasDisponiveis == []

    def cadastrar(self):
        pass


    def adicionarApp(self, App):
        #App._torre = self
        App._torre = self._nome
        self._Apartamentos.append(App)

    def listarApartamentos(self):
        print("\nListando apartamentos da Torre {}".format(self._nome))
        i = 1
        for app in self._Apartamentos:
            print("{} -- ID: {} -- NUMERO: {} -- TORRE: {} -- VAGA: {}".format(i, app._id, app._numero, self._nome, app.vaga))
            i += 1

    def imprimirQueue(self):
        pass

    def imprimirSelf(self):
        pass



#CRIANDO FILA - QUEUE DOS APARTAMENTOS DO BLOCO A
filaBlocoA = Queue()


#CRIANDO APARTAMENTOS
app1 = Apartamento(23, 1)
app2 = Apartamento(11, 2)
app3 = Apartamento(5, 3)
app4 = Apartamento(23, 4)
app5 = Apartamento(11, 5)
app6 = Apartamento(16, 6)
app7 = Apartamento(32, 7)
app8 = Apartamento(12, 8)


blocoA =  Torre(2, "bloco A", "rua doze")
blocoA.adicionarApp(app1)
blocoA.adicionarApp(app2)
blocoA.adicionarApp(app3)
blocoA.adicionarApp(app4)
blocoA.adicionarApp(app5)
blocoA.adicionarApp(app6)
blocoA.adicionarApp(app7)
blocoA.adicionarApp(app8)
blocoA.listarApartamentos()


print("\nInformações dos Apartamentos")
app1.imprimirSelf()
app2.imprimirSelf()
app3.imprimirSelf()
app4.imprimirSelf()
app5.imprimirSelf()
app6.imprimirSelf()
app7.imprimirSelf()
app8.imprimirSelf()



#POPULANDO FILAVAGAS DO BLOCOA
filaBlocoA.enqueue(app1)
filaBlocoA.enqueue(app2)
filaBlocoA.enqueue(app3)
filaBlocoA.enqueue(app4)
filaBlocoA.enqueue(app5)
filaBlocoA.enqueue(app6)
filaBlocoA.enqueue(app7)
filaBlocoA.enqueue(app8)


#MOSTRANDO A FILA DE APPS DO BLOCO A
filaBlocoA.showQueue()

#CHAMANDO FUNÇÃO PARA ATRIBUIR VAGAS PARA QUEM ESTA NA FILA
filaBlocoA.__iter__()


print("\nInformações dos Apartamentos")
app1.imprimirSelf()
app2.imprimirSelf()
app3.imprimirSelf()
app4.imprimirSelf()
app5.imprimirSelf()
app6.imprimirSelf()
app7.imprimirSelf()
app8.imprimirSelf()


#------------------------------------------------- bloco b -----------------------------------------

blocoB =  Torre(4, "bloco B", "rua treze")
filaBlocoB = Queue()
app8bB = Apartamento(23, 8)
app14bB = Apartamento(26, 14)


blocoB.adicionarApp(app8bB)
blocoB.adicionarApp(app14bB)
filaBlocoB.enqueue(app8bB)
filaBlocoB.enqueue(app14bB)
blocoB.listarApartamentos()
filaBlocoB.showQueue()
filaBlocoB.__iter__()
blocoB.listarApartamentos()



