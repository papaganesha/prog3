import random
#print(random.randint(1, 100))




# FILA --------------------------------------------------------------------------------

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

    def bringITback(self, vaga):
        self._vagasDisponiveis.append(vaga)


    def __iter__(self):
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

    def vagasDisponiveis(self):
        return self._vagasDisponiveis

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
            i += 1

    def enqueue(self, item):
        check = self.isEmpty()
        if check == True:
            self.items.insert(0, item)
        else:
            self.items.append(item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)




# APARTAMENTO ----------------------------------------------------------------------------------


class Apartamento:
    def __init__(self, id, numero, torre = None):
        self._id = id
        self._numero = numero
        self._torre = torre
        self.vaga = 0

    def __iter__(self):
        return self


    def devolverVaga(self):
        retorno = self.vaga
        self.vaga = None
        return retorno
        
    def alterarVaga(self, valor):
        valorInt = int(valor)
        self.vaga = valorInt


    def imprimirSelf(self):
        id = self._id
        numero = self._numero
        torre = self._torre
        vaga = self.vaga
        print("APP N:{} ---- BLOCO:{} ---- VAGA:{}".format(numero, torre._nome, vaga))







class Torre:
    def __init__(self, id:int, nome:str, endereco:str):
        self._id = id
        self._nome = nome
        self._endereco = endereco


# RODANDO -------------------------------------------------------------------------------------

#CRIANDO BLOCO B
blocoA =  Torre(1, "bloco A", "rua doze")

#ESPECIFICANDO A FILA, PARA SEREM COLOCADOS APENAS OS APARTAMENTOS DO BLOCO A
filaBlocoA = Queue()

#CRIANDO APARTAMENTOS BLOCO A
app1_BA = Apartamento(1, 1, blocoA)
app2_BA = Apartamento(2, 2, blocoA)
app3_BA = Apartamento(2, 3, blocoA)
app4_BA = Apartamento(3, 4, blocoA)
app5_BA = Apartamento(5, 5, blocoA)


#CRIANDO BLOCO B
blocoB =  Torre(2, "bloco B", "rua doze")

#ESPECIFICANDO A FILA, PARA SEREM COLOCADOS APENAS OS APARTAMENTOS DO BLOCO B
filaBlocoB = Queue()

#CRIANDO APARTAMENTOS BLOCO B
app1_BB = Apartamento(11, 11, blocoB)
app2_BB = Apartamento(12, 12, blocoB)
app3_BB = Apartamento(13, 13, blocoB)
app4_BB = Apartamento(14, 14, blocoB)
app5_BB = Apartamento(15, 15, blocoB)

#ADICIONANDO APPS DO BLOCO A NA FILA
filaBlocoA.enqueue(app1_BA)
filaBlocoA.enqueue(app2_BA)
filaBlocoA.enqueue(app3_BA)
filaBlocoA.enqueue(app4_BA)
filaBlocoA.enqueue(app5_BA)


#ADICIONANDO APPS DO BLOCO B NA FILA
filaBlocoB.enqueue(app1_BB)
filaBlocoB.enqueue(app2_BB)
filaBlocoB.enqueue(app3_BB)
filaBlocoB.enqueue(app4_BB)
filaBlocoB.enqueue(app5_BB)



#MOSTRANDO FILAS
filaBlocoA.showQueue()
filaBlocoB.showQueue()


#MOVENDO FILA E ATRIBUINDO VAGAS
filaBlocoA.__iter__()
filaBlocoB.__iter__()



#MOSTRANDO APARTAMENTOS APOS A ATRIBUIÇÃO DE VAGAS
app1_BA.imprimirSelf()
app1_BB.imprimirSelf()


#VERFICANDO VAGAS DISPONIVEIS NA FILA B
print(filaBlocoB.vagasDisponiveis())

#DEVOLVENDO VAGA
vagaTo = app1_BB.devolverVaga()
filaBlocoB.bringITback(vagaTo)


#VERFICANDO VAGAS DISPONIVEIS NA FILA B
print(filaBlocoB.vagasDisponiveis())

#MOSTRANDO APARTAMENTO QUE DEVOLVEU A VAGA
app1_BB.imprimirSelf()

















class Queue:
    def __init__(self):
        self.items = []


    def isEmpty(self):
        return self.items == []

    def showQueue(self):
        print("\nFila de Apartamentos esperando vaga")
        i = 1
        for itens in self.items:
            print("{} --  APP N: {}".format(i, itens._numero))
            i += 1

    def enqueue(self, item):
        check = self.isEmpty()
        if check == True:
            self.items.insert(0, item)
        else:
            self.items.append(item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


