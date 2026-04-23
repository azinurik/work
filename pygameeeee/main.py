import pygame
pygame.init()


screen = pygame.display.set_mode((700, 400))
pygame.display.set_caption("My game")
icon = pygame.image.load("images/image.png").convert_alpha()
pygame.display.set_icon(icon)


bground = pygame.image.load("images/bggame.png").convert_alpha()
player = pygame.image.load("images/right_player/rp1.png").convert_alpha()

run = True
while run:
    screen.blit(bground, (0, 0))  
    screen.blit(player, (50, 200))  

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

