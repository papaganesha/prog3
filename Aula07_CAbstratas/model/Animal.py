from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):

    @property
    def idade(self):
        pass

    @idade.setter
    @abstractmethod
    def idade(self, newIdade):
        pass


    @abstractmethod
    def cadastrar(self):
        pass


