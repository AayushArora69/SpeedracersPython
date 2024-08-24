import pygame
pygame.init()

HEIGHT = 1280
WIDTH = 720

screen = pygame.display.set_mode((HEIGHT, WIDTH))
title = pygame.display.set_caption("Game")
running = True

red = (255,0,0)
blue = (0,0,255)
black = (0,0,0)
magenta = (255,0,255)
yellow = (255,255,0)

screen.fill(red)
pygame.draw.rect(screen, yellow, (400, 250, 500, 250))
while(running):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()