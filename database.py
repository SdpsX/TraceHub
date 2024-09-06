import mysql.connector
from mysql.connector import Error
from config import db_config

def connect_to_db():
    try:
        conn = mysql. connector.connect(**db_config)
        return conn
    except Error  as e :
        print(f"Ошибка подключения к базе данных: {e}")
        return None