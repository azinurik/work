# connect.py

import psycopg2
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT

def get_connection():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT,
            client_encoding='UTF8'  # исправляем ошибку Unicode
        )
        print("Подключение прошло успешно!")
        return conn
    except Exception as e:
        print("Ошибка подключения:", e)
        return None