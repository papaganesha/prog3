

class Conta:
    def __init__(self):
        self.__saldo = 0.0


    def __descontarTarifa(self):
        self.__saldo -=1.99


    def depositar(self, valor):
        self.__saldo +=valor
        self.__descontarTarifa()


    def sacar(self, valor):
        if(self.__saldo - 1.99 >= valor):
            self.__saldo +=valor
            self.__descontarTarifa()


    def getSaldo(self):
        return self.__saldo


    def setSaldo(self, valor):
        self.__saldo = valor



    def imprimirSaldo(self):
        print("O saldo é: {}".format(self.__saldo))




c1 = Conta()

c1.imprimirSaldo()



c1.depositar( 10.5 )

c1.imprimirSaldo()



c1.sacar( 5.2 )

c1.imprimirSaldo()



c1.setSaldo(20)

c1.imprimirSaldo()

