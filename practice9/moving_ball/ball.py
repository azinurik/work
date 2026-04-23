import pygame

class Ball:
    def __init__(self):
        self.x = 300
        self.y = 200
        self.radius = 25
        self.speed = 20

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)