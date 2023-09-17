import pymysql

from config import mysql

def get_sorvetes_by_categoria(id_categoria):
    print(id_categoria)
    return execute("SELECT * FROM sorvetes WHERE id_categoria = %s", (id_categoria), fetch_all)

def get_categorias():
    return execute("SELECT * FROM categoria", None, fetch_all)

def execute(sql, parameters, callback):
    with mysql.connect() as conn:
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            if parameters is None:
                cursor.execute(sql)
                return callback(cursor)
            else:
                cursor.execute(sql, parameters)
                return callback(cursor)

def fetch_all(cursor):
    return cursor.fetchall()

def fetch_one(cursor):
    return cursor.fetchone()