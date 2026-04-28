import pygame
import random
import json
from config import *

def load_settings():#читает JSON (цвет змейки, звук и т.д.)
    try:
        with open(SETTINGS_PATH) as f:
            return json.load(f)
    except:
        return {"snake_color": [0,200,0], "grid": True, "sound": True}

def save_settings(s):
    with open(SETTINGS_PATH, "w") as f:
        json.dump(s, f)

class Game: #управляет всей игрой
    def __init__(self, screen, pid, best):
        self.screen = screen
        self.pid = pid
        self.best = best
        self.font = pygame.font.SysFont(None, 26)

        self.settings = load_settings()
        self.reset()

    def reset(self):
        self.snake = [(COLS//2, ROWS//2)]
        self.dir = (1,0)
        self.next_dir = (1,0)

        self.score = 0
        self.level = 1
        self.eaten = 0

        self.base_speed = 8
        self.speed = self.base_speed

        self.over = False

        self.foods = []
        self.obstacles = []
        self.powerup = None

        self.active_pu = None
        self.pu_end = 0
        self.shield = False

        self.spawn_food()

    def free_cell(self):#ищет свободную клетку (не занята змейкой, едой и т.д.)
        taken = set(self.snake + self.obstacles)
        for f in self.foods:
            taken.add((f[0],f[1]))
        if self.powerup:
            taken.add((self.powerup[0],self.powerup[1]))

        for _ in range(300):
            x = random.randint(1,COLS-2)
            y = random.randint(1,ROWS-2)
            if (x,y) not in taken:
                return x,y
        return None

    def spawn_food(self):#создаёт еду:
        pos = self.free_cell()
        if not pos: return
        x,y = pos

        r = random.random()
        if r < 0.15:
            t, pts = "poison", 0
        elif r < 0.4:
            t, pts = "heavy", 3
        else:
            t, pts = "normal", 1

        self.foods.append([x,y,t,pts,pygame.time.get_ticks()])

    def spawn_powerup(self):#бонус:
        pos = self.free_cell()
        if not pos: return
        x,y = pos
        self.powerup = [x,y,random.choice(["speed","slow","shield"]),pygame.time.get_ticks()]

    def spawn_obstacles(self):#генерирует препятствия
        self.obstacles = []
        hx,hy = self.snake[0]

        count = 3 + self.level
        for _ in range(500):
            if len(self.obstacles) >= count:
                break
            x = random.randint(1,COLS-2)
            y = random.randint(1,ROWS-2)

            if abs(x-hx)<3 and abs(y-hy)<3:
                continue

            self.obstacles.append((x,y))

    def handle_input(self,event):#управление стрелками
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.dir!=(0,1):
                self.next_dir=(0,-1)
            if event.key == pygame.K_DOWN and self.dir!=(0,-1):
                self.next_dir=(0,1)
            if event.key == pygame.K_LEFT and self.dir!=(1,0):
                self.next_dir=(-1,0)
            if event.key == pygame.K_RIGHT and self.dir!=(-1,0):
                self.next_dir=(1,0)
    
    #каждый кадр:

    #двигает змейку
    #проверяет столкновения
    #проверяет еду
    #проверяет бонусы

    def update(self):
        now = pygame.time.get_ticks()

        if now - getattr(self,'last',0) < 1000//self.speed:
            return
        self.last = now

        self.dir = self.next_dir
        hx,hy = self.snake[0]
        dx,dy = self.dir
        nx,ny = hx+dx,hy+dy#Движение

        # walls
        if nx<0 or nx>=COLS or ny<0 or ny>=ROWS:#Проверка стен
            if self.shield:
                self.shield=False
            else:
                self.over=True
                return

        # obstacles
        if (nx,ny) in self.obstacles:
            if not self.shield:
                self.over=True
                return
            self.shield=False

        # self
        if (nx,ny) in self.snake:
            if not self.shield:
                self.over=True
                return
            self.shield=False

        self.snake.insert(0,(nx,ny))
        grow=False

        # food
        for f in self.foods[:]:
            if (f[0],f[1])==(nx,ny):#Проверка еды
                if f[2]=="poison":
                    for _ in range(2):
                        if len(self.snake)>1:
                            self.snake.pop()
                    if len(self.snake)<=1:
                        self.over=True
                        return
                else:
                    self.score+=f[3]
                    self.eaten+=1
                    grow=True

                self.foods.remove(f)
                self.spawn_food()

                if self.eaten%5==0:#Уровни
                    self.level+=1
                    self.speed=min(20,self.speed+1)
                    if self.level>=3:
                        self.spawn_obstacles()
                break

        if not grow:
            self.snake.pop()

        # powerup
        if self.powerup and (self.powerup[0],self.powerup[1])==(nx,ny):
            t=self.powerup[2]
            self.active_pu=t

            if t=="speed":
                self.speed=self.base_speed+4
                self.pu_end=now+5000
            elif t=="slow":
                self.speed=max(3,self.base_speed-3)
                self.pu_end=now+5000
            else:
                self.shield=True

            self.powerup=None

        if self.active_pu in ("speed","slow") and now>self.pu_end:
            self.speed=self.base_speed
            self.active_pu=None

        if not self.powerup and random.random()<0.01:
            self.spawn_powerup()

    def draw(self):
        self.screen.fill(BLACK)

        # grid
        if self.settings.get("grid"):
            for x in range(0,WIDTH,CELL):
                pygame.draw.line(self.screen,GRAY,(x,0),(x,HEIGHT))
            for y in range(0,HEIGHT,CELL):
                pygame.draw.line(self.screen,GRAY,(0,y),(WIDTH,y))

        # obstacles
        for ox,oy in self.obstacles:
            pygame.draw.rect(self.screen,GRAY,(ox*CELL,oy*CELL,CELL,CELL))

        # food
        colors={"normal":RED,"heavy":ORANGE,"poison":DARK_RED}
        for f in self.foods:
            pygame.draw.rect(self.screen,colors[f[2]],(f[0]*CELL,f[1]*CELL,CELL,CELL))

        # powerup
        if self.powerup:
            col={"speed":YELLOW,"slow":BLUE,"shield":PURPLE}[self.powerup[2]]
            pygame.draw.rect(self.screen,col,(self.powerup[0]*CELL,self.powerup[1]*CELL,CELL,CELL))

        # snake
        sc=self.settings.get("snake_color",[0,200,0])
        for i,(x,y) in enumerate(self.snake):
            pygame.draw.rect(self.screen,WHITE if i==0 else sc,(x*CELL,y*CELL,CELL,CELL))

        # HUD
        self.screen.blit(self.font.render(f"Score:{self.score} Level:{self.level} Best:{self.best}",True,WHITE),(5,5))