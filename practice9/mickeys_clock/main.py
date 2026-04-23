import pygame
from clock import MickeyClock

pygame.init()

W, H = 800, 800
screen = pygame.display.set_mode((W, H))

icon=pygame.image.load('practice9/mickeys_clock/images/icon.png')
pygame.display.set_icon(icon)
 
clock = pygame.time.Clock()
app = MickeyClock(W, H)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    app.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()