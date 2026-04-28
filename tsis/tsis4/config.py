import os # для работы с файлами и путями

WIDTH = 600 # ширина окна
HEIGHT = 600# высота окна
CELL = 20 # размер одной клетки (grid)

# сколько клеток по горизонтали и вертикали
COLS = WIDTH // CELL
ROWS = HEIGHT // CELL

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
DARK_RED = (120, 0, 0)
GRAY = (100, 100, 100)
YELLOW = (255, 220, 0)
BLUE = (0, 100, 255)
PURPLE = (150, 0, 200)
ORANGE = (255, 140, 0)

# DB config
DB = {
    "dbname": "snake",
    "user": "postgres",
    "password": "1234",
    "host": "localhost",
    "port": 5432
}
# путь к текущей папке проекта
BASE_DIR = os.path.dirname(__file__)
# путь к звуку
SOUND_PATH = os.path.join(BASE_DIR, "eat.wav")
# путь к файлу настроек
SETTINGS_PATH = os.path.join(BASE_DIR, "settings.json")