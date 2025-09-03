import os
import psycopg2
from dotenv import load_dotenv
from contextlib import contextmanager

load_dotenv()

DATABASE = os.getenv("DATABASE")
HOST = os.getenv("HOST")
USERSERVER = os.getenv("USERSERVER")
PASSWORD = os.getenv("PASSWORD")
PORT = os.getenv("5432")

@contextmanager
def instance_cursor():
    connection = psycopg2.connect(database = DATABASE, host = HOST, user = USERSERVER, password = PASSWORD, port = PORT)
    cursor = connection.cursor()
    try:
        yield cursor
        
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("Conexão encerrada com PostgreSQL")

def consulta_geral():
    with instance_cursor() as cursor:
        query = '''
        SELECT * FROM REGISTROS
        '''
        cursor.execute(query, )
        request = cursor.fetchall() # Fetchall pega tudo do excute, devolve todo o que achar.
        return request
    
def consulta_nome(user):
    with instance_cursor() as cursor:
        query = '''
            SELECT nome, usuario, senha FROM REGISTRO WHERE usuario = %s
        '''
        cursor.execute(query, (user, ))
        request = cursor.fetchall()
        return request

def cria_tabela():
    connection = psycopg2.connect(database = DATABASE, host = HOST, user = USERSERVER, password = PASSWORD, port = PORT)
    cursor = connection.cursor()

    query = '''
        CREATE TABLE REGISTRO (
            nome varchar (30),
            usuario varchar (30),
            senha varchar (100),
        )
        '''
    cursor.execute(query)
    connection.commit()
    print("Tabela Criada")
    if (connection):
        cursor.close()
        connection.close()
        print("Conexão com PostgreSQL Encerrada")

def add_registro(nome, user, senha):
    connection = psycopg2.connect(database = DATABASE, host = HOST, user = USERSERVER, password = PASSWORD, port = PORT)
    cursor = connection.cursor()

    query = f'''
        INSERT INTO REGISTROS VALUES
        {nome, user, senha}
        '''
    cursor.execute(query)
    connection.commit()
    print("Valores inseridos com sucesso")
    if (connection):
        cursor.close()
        connection.close()
        print("Conexão com PostgreSQL Encerrada")
        