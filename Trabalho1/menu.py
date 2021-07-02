from Torre import *



menu = '''
0 - TERMINAR
1 - ADICIONAR TORRE
2 - ADICIONAR APARTAMENTOS(POR TORRE NOME)
4 - ADICIONAR APARTAMENTOS(POR TORRE ID)
5 - ADICIONAR APARTAMENTO(S) A FILA
6 - VER FILA 
7 - GIRAR FILA
8 - DEVOLVER VAGA
9 - TERMINAR
ESCOLHA SEU CODIGO:
'''

apartamentos = []
torres = []
filas = []


def loopMenu():
    while True:
        try:
            escolha = int(input(menu))
            if escolha == 0 or escolha == 9:
                print("Finished")
                break
            elif escolha == 1:
                print("ADICIONAR TORRE")
                idTorre = int(input("Digite o ID da Torre:"))
                nomeTorre = str(input("Digite o nome da Torre: "))
                enderecoTorre = str(input("Digite o endereço da Torre: "))
                if (idTorre and nomeTorre and enderecoTorre):
                    torreInstancia = Torre(idTorre, nomeTorre, enderecoTorre)
                    torres.append(torreInstancia)
                else:
                    input("Insira as informações corretamente")


            elif escolha == 2:
                print("ADICIONAR APARTAMENTO POR NOME TORRE")
                torreNome = input("Digite o NOME da Torre do Apartamento")
                torreOBJ = 0
                for torre in torres:
                    if torre._nome == torreNome:
                        torreOBJ = torre
                if torreOBJ != None:
                    idApartamento = int(input("Digite o ID do Apartamento: "))
                    numeroApartamento = int(input("Numero do Apartamento: "))
                    appInstancia = Apartamento(idApartamento, numeroApartamento, torreOBJ)
                    apartamentos.append(appInstancia)

                else:
                    print("Torre de NOME: {} não existe".format(nomeTorre))




            elif escolha == 3:
                print("ADICIONAR APARTAMENTO POR ID TORRE")
                torreID = input("Digite o ID da Torre do Apartamento")
                torreOBJ = 0
                for torre in torres:
                    if torre._id == torreID:
                        torreOBJ = torre
                if torreOBJ != None:
                    idApartamento = int(input("Digite o ID do Apartamento: "))
                    numeroApartamento = int(input("Numero do Apartamento: "))
                    appInstancia = Apartamento(idApartamento, numeroApartamento, torreOBJ)
                    apartamentos.append(appInstancia)

                else:
                    print("Torre de ID: {} não existe".format(nomeTorre))




            elif escolha == 3:
                print("ADICIONAR APARTAMENTO A FILA")

            elif escolha == 4:
                print("VER FILA")


            elif escolha == 5:
                print("GIRAR FILA")


            else:
                print("CODIGO {} INDISPONIVEL".format(escolha))


        except:
            print("Codigo de menu deve ser numerico")


loopMenu()
print(torres[0]._nome)
print(apartamentos[0]._numero, apartamentos[0]._torre._nome)

