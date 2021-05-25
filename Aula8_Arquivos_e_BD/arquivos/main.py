import os

file = open("ola.txt", "rt")
print(file.read())

#----------- WRITE ---------------------------------------

print('\n----------- WRITE ---------------------------------------')
file_to_append = open('anexado.txt', 'w')
file_to_append.write('''
Esse texto foi escrito por      __  ___      ______     
                               /  |/  /___ _/ ____/_  __
                              / /|_/ / __ `/ /_  / / / /
                             / /  / / /_/ / __/ / /_/ / 
                            /_/  /_/\__,_/_/    \__,_/ 

''')
file_to_append.close()


file_to_read = open('anexado.txt', 'r')
print("\n",file_to_read.read())


#----------- APPEND ---------------------------------------

print('\n----------- APPEND ---------------------------------------')
file_to_append = open('anexado.txt', 'a')
file_to_append.write('Essa escrita foi apendada')
file_to_append.close()

file_to_read = open('anexado.txt', 'r')
print("\n",file_to_read.read())


#----------- DELETE/REMOVE ---------------------------------------

print('\n----------- DELETE/REMOVE ---------------------------------------')

if os.path.exists("novo.txt"):
    os.remove("novo.txt")
    print("Arquivo Removido")

else:
    print("Arquivo nao encontrado")
    
    
    
def criar_txt(nome_txt, texto_txt):
    print('\nCriar arquivo txt')
    file = open("{}".format(nome_txt), "wt")
    file.write(texto_txt)
    print("Arquivo {} criado".format(nome_txt))
    
    
def ler_txt(nome_txt):
    try:
        if nome_txt != "":
            print('\nLeitura de arquivo ({})'.format(nome_txt))
            file = open("{}".format(nome_txt), "rt")
            print(file.read())
    except Exception as e:
        print(e)


    

criar_txt("test.txt", "Esse txt foi criado atraves de uma funcao")
ler_txt('te.txt')
ler_txt('test.txt')