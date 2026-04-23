import pygame
from ball import Ball

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Moving Ball")

clock = pygame.time.Clock()
ball = Ball()

running = True

while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and ball.x - 25 > 0:
        ball.move(-20, 0)
    if keys[pygame.K_RIGHT] and ball.x + 25 < 800:
        ball.move(20, 0)
    if keys[pygame.K_UP] and ball.y - 25 > 0:
        ball.move(0, -20)
    if keys[pygame.K_DOWN] and ball.y + 25 < 600:
        ball.move(0, 20)

    ball.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()