#AULA1 -- 3SEMESTRE

#08/03/21
#21:45 - 1 alteracao
#22:48 - 2 alteracao
#23:16 - 3 alteracao



#Exercicio
#Construir um algoritmo que contenha 3 listas:
#Nomes de produtos, precos de cada produto, quantidade de cada produto
#Construir uma funcao para imprimir um dos produtos da lista e uma funcao para retirar um produto da lista



LstProdutos2 = ["PEPSI", "FEIJAO", "ARROZ", "BOLACHA"]
LstPrecos = [3.5, 4.0, 4.25, 2.0]
LstQtd = [15, 20,30, 40]

def forListaProdutos():
    print("\n----- LISTA DE PRODUTOS -----")
    cont = 0
    for produto in LstProdutos2:
        cont +=1
        print(cont,"-", produto)
    


def escolhaProduto(produto_index):
    produto_index = produto_index - 1
    print("\nProduto de Index({}) \nNome: {} \nPreco: {} \nQtdade: {}".format(produto_index+1, LstProdutos2[produto_index], LstPrecos[produto_index], LstQtd[produto_index]))
    

def retornarEscolha():
    input("\nRetornar ao MENU, press[ENTER]")
    escolha()


def adicionarProduto():
    try:   
        nomeProduto = str(input("Nome do produto:"))
        precoProduto = float(input("Preco do produto:"))
        qtdProduto = int(input("Qtde de produto:"))

        LstProdutos2.append(nomeProduto)
        LstPrecos.append(precoProduto)
        LstQtd.append(qtdProduto)
    except:
        print("Voce preencheu alguma informacao com valor numerico ou simbolico incorretamente")

def excluiProduto(produto_index):
    produto_index = produto_index - 1
    LstProdutos2.pop(produto_index)
    LstPrecos.pop(produto_index)
    LstQtd.pop((produto_index))
    print("Produto de Index({}) foi excluido com sucesso".format(produto_index+1))
    


def menu():
    menu = '''
------------ MENU ------------
1 - Mostrar lista de Produtos
2 - Mostrar Produto
3 - Adicionar Produto
4 - Excluir Produto
5 - Sair 

Escolha:
'''

    return menu

def escolha():
    while True:
        try:
            escolha = input(menu())
            if escolha == "1":
                forListaProdutos()
                retornarEscolha()

            elif escolha == "2":
                print("\n------------ MOSTRA DE PRODUTO ------------")
                indexChoice = int(input("Index do Produto:"))
                escolhaProduto(indexChoice)
                retornarEscolha()

            elif escolha == "3":
                print("\n------------ ADICIONAR PRODUTO ------------")
                adicionarProduto()
                retornarEscolha()

            elif escolha == "4":
                print("\n------------ EXCLUIR PRODUTO ------------")
                indexChoice = int(input("Index do Produto:"))
                excluiProduto(indexChoice)
                retornarEscolha()
            elif escolha == "5" or escolha == "0":
                print("Até mais")
                break
        except:
            print("Voce preencheu alguma informacao com valor numerico ou simbolico incorretamente")


escolha()