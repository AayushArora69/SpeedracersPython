import pygame
pygame.init()

HEIGHT = 1280
WIDTH = 720

screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Bitting Images")

rocket_image = pygame.image.load(r"E:\GitHub GameDev\SpeedracersPython\Scripts\rocket.png")
rocket_rect = rocket_image.get_rect()
rocket_rect.topleft = (0,0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0,0,255))  
        
    screen.blit(rocket_image, rocket_rect)
    pygame.draw.line(screen, (0,0,0), (0,350), (HEIGHT, 350), 10)
    pygame.draw.rect(screen, (255, 165, 0), (0, 355, HEIGHT, 600))
    pygame.display.update()
pygame.quit()
