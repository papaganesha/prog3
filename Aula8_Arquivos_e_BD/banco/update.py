# encoding: utf-8
from connect_db import *
from consultar import *


from connect_db import *

def updateProduto():
    try:
        if conn.is_connected():
            print('\nAlterar de produtos')
            ID = int(input('ID do produto: '))
            produto = retornar_Produtos_IDfilter(ID)
            nome = str(input("Nome {} ➯ ".format(produto[1]))).upper()
            preco = float(input('Preco {} ➯ '.format(produto[2])))
            quantidade = int(input('Quantidade {} ➯ '.format(produto[3])))
            if nome != "":
                if preco != 0 and preco > 0 and preco != "":
                   if quantidade != 0  and quantidade > 0 and quantidade != "":
                        query = 'UPDATE produto SET nome = %s, preco = %s , quantidade = %s where id = %s'
                        data = [nome, preco, quantidade, ID]
                        cursor.execute(query, data)
                        conn.commit()
                        print('Produto Alterado com sucesso')
                   else:
                           query = 'UPDATE produto SET nome = %s, preco = %s  where id = %s'
                           data = [nome, preco, ID]
                           cursor.execute(query, data)
                           conn.commit()
                           print('Produto Alterado com sucesso')
                else:
                        query = 'UPDATE produto SET nome = %s, quantidade = %s where id = %s'
                        data = [nome, quantidade, ID]
                        cursor.execute(query, data)
                        conn.commit()
                        print('Produto Alterado com sucesso')
            else:
                query = 'UPDATE produto SET  preco = %s , quantidade = %s where id = %s'
                data = [preco, quantidade, ID]
                cursor.execute(query, data)
                conn.commit()
                print('Produto Alterado com sucesso')

    except Exception as e:
        print(e)
        updateProduto()




