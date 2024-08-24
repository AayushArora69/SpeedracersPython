import pygame
pygame.init()

HEIGHT = 1280
WIDTH = 720
screen = pygame.display.set_mode((HEIGHT, WIDTH))
caption = pygame.display.set_caption("Continous Keyboard Movement!")
#defining colors

BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
#load images

image = pygame.image.load(r"C:\Users\fkmic\Downloads\adhee cameo.png")
#player variables

speed = 25
scale_factor = 0.35

scaled_x = scale_factor * HEIGHT
scale_y = scale_factor * WIDTH

adhee_image = pygame.transform.scale(image, (scaled_x, scale_y))
adhee = adhee_image.get_rect()
adhee.x = 35
adhee.y = 50

running = True
while(running == True):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
        screen.fill(BLUE)
        screen.blit(adhee_image, adhee)
        pygame.display.update()
pygame.quit()