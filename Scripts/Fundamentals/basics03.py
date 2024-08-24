import pygame
import random
pygame.init()

height = 1280
width = 720

#Colors
GREEN = (0,255,0)
BLUE = (0,0,255)
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
RANDOM = ((random.choice(0,255), random.choice(0,255), random.choice(0,255)))

screen = pygame.display.set_mode((height, width))
pygame.display.set_caption("Blitting Text!")
running = True

font = pygame.font.get_fonts()
system_font = pygame.font.SysFont("GROBOLD", 64, bold=False, italic=False)
current_font = system_font.render("Hello world!", True, RED, BLACK)
current_rect = current_font.get_rect()
current_rect.center = (height//2, width//2)


while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
    screen.fill(GREEN)
    screen.blit(current_font, current_rect)
    pygame.display.update()

pygame.quit()