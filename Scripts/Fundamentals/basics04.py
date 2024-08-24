import pygame
pygame.init()

RED = (255,0,0)
BLUE = (0, 0, 255)
running = True
HEIGHT = 1280
WIDTH = 720
screen = pygame.display.set_mode((HEIGHT, WIDTH))

font = pygame.font.SysFont("Calibri", 64, bold=True, italic=False)
render_font = font.render("Hello world!", True, RED)
font_rect = render_font.get_rect()
font_rect.center = (HEIGHT // 2, WIDTH // 2) #x, y co-ordinates

while(running == True):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
        
        pygame.display.update()
        screen.fill(BLUE)
        screen.blit(render_font, font_rect)
pygame.quit()