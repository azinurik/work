import psycopg2
from config import DB

def connect():
    return psycopg2.connect(**DB)

def init_db():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS players (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS game_sessions (
            id SERIAL PRIMARY KEY,
            player_id INTEGER REFERENCES players(id),
            score INTEGER NOT NULL,
            level_reached INTEGER NOT NULL,
            played_at TIMESTAMP DEFAULT NOW()
        )
    """)

    conn.commit()
    cur.close()
    conn.close()
#Получить или создать игрока
def get_or_create_player(name):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT id FROM players WHERE username=%s", (name,))
    row = cur.fetchone()

    if row:
        pid = row[0]
    else:
        cur.execute(
            "INSERT INTO players (username) VALUES (%s) RETURNING id",
            (name,)
        )
        pid = cur.fetchone()[0]
        conn.commit()

    cur.close()
    conn.close()
    return pid
#Сохранить результат
def save_result(pid, score, level):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO game_sessions (player_id, score, level_reached)
        VALUES (%s, %s, %s)
    """, (pid, score, level))

    conn.commit()
    cur.close()
    conn.close()
#Таблица лидеров
def get_leaderboard():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT p.username, s.score, s.level_reached, s.played_at
        FROM game_sessions s
        JOIN players p ON p.id = s.player_id
        ORDER BY s.score DESC, s.level_reached DESC
        LIMIT 10
    """)

    data = cur.fetchall()
    cur.close()
    conn.close()
    return data
#Лучший результат
def get_best(pid):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT MAX(score) FROM game_sessions WHERE player_id=%s", (pid,))
    row = cur.fetchone()

    cur.close()
    conn.close()

    return row[0] if row and row[0] else 0