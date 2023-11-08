import pymysql

from config import mysql
from flask import session
import functools

def get_sorvetes_by_categoria(id_categoria):
    return execute("SELECT * FROM sorvetes WHERE id_categoria = %s", (id_categoria), fetch_all)

def get_sorvetes_by_id(id):
    return execute("SELECT * FROM sorvetes WHERE id = %s", (id), fetch_one)

def get_categorias():
    return execute("SELECT * FROM categoria", None, fetch_all)

def add_item_carrinho(sorvete, qtd):
    if 'carrinho' not in session:
        session['carrinho'] = []
    carrinho = session['carrinho']

    exist = False
    for item in carrinho:
        if(item['id'] == sorvete['id']):
            item['qtd'] = int(item['qtd']) + 1
            exist = True
    if exist == False:
        carrinho.append(
            {
                "id": sorvete['id'],
                "nome": sorvete['nome'],
                "qtd": qtd,
                "img": sorvete['url_img'],
                "preco":  sorvete['preco']
            }
        )

    session['carrinho'] = carrinho

    return session['carrinho']


def get_carrinho():
    if 'carrinho' not in session:
        session['carrinho'] = []
        
    total = 0
    qtd_total = 0
    if len(session['carrinho']) > 0:
        sub = list(map(lambda item: int(item["qtd"]) * float(item["preco"]), session['carrinho']))
        total = functools.reduce(lambda a, b: a+b, sub)
        sub = list(map(lambda item: int(item["qtd"]), session['carrinho']))
        qtd_total = functools.reduce(lambda a, b: a+b, sub)

    return (session['carrinho'], total, qtd_total)


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