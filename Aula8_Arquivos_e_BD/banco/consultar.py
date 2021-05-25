from connect_db import *

def Consultar_Produtos():
    try:
        if conn.is_connected():
            print('\nConsulta de Produtos')
            print('ID - NOME, PRECO, QUANTIDADE')
            print('-----------------------------------')
            query = 'SELECT * FROM produto'
            cursor.execute(query)
            Rset = cursor.fetchall()
            for i in Rset:
                #print(i)
                print(str(i[0])+" - "+i[1]+" - "+str(i[2])+ " - "+str(i[3]))
                print('-----------------------------------')
        else:
            print(Exception)

    except Exception as e:
        print(e)


def Consultar_Produtos_IDfilter(ID):
    try:
        if conn.is_connected():
            print('\nConsulta de Produtos por ID({})'.format(ID))
            print('ID - NOME, PRECO, QUANTIDADE')
            print('-----------------------------------')
            query = "SELECT * FROM produto WHERE id = "+str(ID)
            cursor.execute(query)
            Rset = cursor.fetchone()
            print(Rset)
            print('-----------------------------------')
            return Rset
        else:
            print(Exception)

    except Exception as e:
        print(e)

def retornar_Produtos_IDfilter(ID):
    try:
        if conn.is_connected():
            query = "SELECT * FROM produto WHERE id = "+str(ID)
            cursor.execute(query)
            Rset = cursor.fetchone()
            return Rset
        else:
            print(Exception)

    except Exception as e:
        print(e)




