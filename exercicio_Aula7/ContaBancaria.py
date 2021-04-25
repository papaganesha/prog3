from abc import ABCMeta, abstractmethod

class ContaBancaria(metaclass=ABCMeta):
    def __init__(self, id, nome):
        self.__id = id
        self._nome = nome

    @abstractmethod
    def cadastrar(self):
        pass

    @property
    def id(self):
        pass

    @id.setter
    @abstractmethod
    def id(self, novo_id):
        pass

    @property
    def nome(self):
        pass

    @nome.setter
    @abstractmethod
    def nome(self, novo_nome):
        pass


    @property
    def saldo(self):
        pass

    @saldo.setter
    @abstractmethod
    def depositar(self, saldo_soma):
        pass

