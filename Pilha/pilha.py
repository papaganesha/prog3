# madeby João Pedro Alves dos Santos
# 10/06/2021 16:26 -- v1


from typing import List, Any

class Pilha:
    def __init__(self):
        self.__dado : List[Any] = []

    # FUNCIONANDO, ADICIONA ITEM NA PILHA
    def adicionarItem(self, item):
        self.__dado.append(item)
        print('{} adicionado na Pilha ✔'.format(item))

    # FUNCIONANDO, MOSTRA OS ITENS DA PILHA
    def __iter__(self):
        print('\nListando itens da Pilha 🔁')
        if len(self.__dado) > 0:
            for i, item in enumerate(self.__dado):
                print('{} - {}'.format(i, item))
        else:
            print('Pilha sem itens\n')


    # FUNCIONANDO, REMOVE O ULTIMO ITEM DA PILHA
    def removerItem(self):
        print('\nRemovendo item da Pilha 🔁')
        if len(self.__dado) > 0:
           self.__dado.pop()
           print('Item removido ✔')
        else:
           print('Sem itens para remover')


    #acontecendo erro, corrigir problema
    def indiceX(self, indice):
        print('\nOlhando item de indice {}'.format(indice))
        if indice > -1 and len(self.__dado) > 0:
               try:
                   if self.__dado[indice] is not IndexError:
                       print('{} -- {}'.format(indice, self.__dado[indice]))
    
               except:
                   print('Item de indice: {} nao existe na pilha'.format(indice))
        else:
            print('Pilha sem itens')


raioVac = Pilha()

#MOSTRANDO OS ITENS DA PILHA
raioVac.__iter__()

#ADICIONANDO 3 ITENS A PILHA
raioVac.adicionarItem('antonio')
raioVac.adicionarItem(27.00)
raioVac.adicionarItem(['coca-cola', 'pepsi'])

#MOSTRANDO OS ITENS DA PILHA
raioVac.__iter__()

#MOSTRANDO ITEM DA PILHA POR INDICE
raioVac.indiceX(2)

#REMOVENDO O ULTIMO ITEM DA PILHA
raioVac.removerItem()

#MOSTRANDO OS ITENS DA PILHA
raioVac.__iter__()

#REMOVENDO O ULTIMO ITEM DA PILHA
raioVac.removerItem()

#MOSTRANDO OS ITENS DA PILHA
raioVac.__iter__()

#REMOVENDO O ULTIMO ITEM DA PILHA
raioVac.removerItem()

#MOSTRANDO OS ITEMS DA PILHA
raioVac.__iter__()


#MOSTRANDO ITEM DA PILHA POR INDICE
raioVac.indiceX(1)