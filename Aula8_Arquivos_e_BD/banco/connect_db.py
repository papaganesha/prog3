import mysql.connector


try:
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        database = 'ap2_banco'
    )
    #print('Banco {} is connected: {}'.format(conn.database, conn.is_connected()))
except:
    print(mysql.connector.errors)


cursor = conn.cursor()