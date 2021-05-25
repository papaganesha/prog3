from connect_db import *

def inserirProduto():
    try:
        if conn.is_connected():
            print('\nInsercao de produtos')
            nome = str(input("Nome: ")).upper()
            preco = float(input('Preco: '))
            quantidade = int(input('Quantidade: '))
            if nome != "" and preco != 0 and preco > 0 and quantidade != 0  and quantidade > 0:
                query = 'INSERT INTO produto(nome, preco, quantidade) VALUES(%s, %s, %s)'
                data = [nome, preco, quantidade]
                cursor.execute(query, data)
                conn.commit()
                cursor.close()
                conn.close()
                print('Produto {} inserido'.format(data[0]))
            else:
                print("Voce digitou algo errado")
                inserirProduto()
    except Exception as e:
        print(e)
        inserirProduto()


