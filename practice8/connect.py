# connect.py

import psycopg2
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT

def get_connection():
    try:
        conn=psycopg2.connect(
            host=DB_HOST,
            name=DB_NAME,
            user=DB_USER,
            pas=DB_PASSWORD,
            port=DB_PORT
        )
        print("Подключение прошло успешно!")
        return conn
    except Exception as e:
        print("Ошибка подключения:", e)
        return None