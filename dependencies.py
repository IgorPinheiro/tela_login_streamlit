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


