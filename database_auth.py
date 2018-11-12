import pymysql

def conecta_banco():

    db = pymysql.connect(address, user, passw, database)
    return db
