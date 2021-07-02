# TENDO NUMERO MAXIMO DE VAGAS DE
import random
from typing import List, Any
from Torre import Torre, Torres
from Apartamento import Apartamento, Apartamentos





#CRIANDO TORRE E INSERINDO EM LISTA DE TORRES
Torre1 = Torre(10, 'BLOCO B', 'RUA DOS BOBOS N 0')
'''Torre1.imprimir()'''
TorresX = Torres()
TorresX.cadastrar(Torre1)
'''TorresX.imprimir()'''


#CRIANDO APARTAMENTO E INSERINDO EM LISTA DE APARTAMENTOS
Ap1 = Apartamento(10, 301, Torre1, None)
Ap2 = Apartamento(10, 304, Torre1, None)
Ap3 = Apartamento(10, 310, Torre1, None)
'''Ap1.imprimir()'''
ApartamentosX = Apartamentos()
ApartamentosX.cadastrar(Ap1)
ApartamentosX.cadastrar(Ap2)
ApartamentosX.cadastrar(Ap3)



'''print(Ap1.getApartamento())
print(Ap2.getApartamento())'''
print(ApartamentosX.getApartamento(4))
print(ApartamentosX.getApartamento(1))


ApartamentosX.imprimir()


for i in ApartamentosX.getApartamentos():
    print(i._numero)







q = Queue()
q.enqueue('hello')
q.enqueue('dog')
q.enqueue(3)
q.dequeue()
