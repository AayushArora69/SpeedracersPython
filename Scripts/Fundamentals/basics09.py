import pygame
pygame.init()
running = True
HEIGHT = 1280
WIDTH = 720
VELOCITY = 10
FPS = 15
clock = pygame.time.Clock()

SCALE_FACTOR = 0.1
screen = pygame.display.set_mode((HEIGHT, WIDTH))
image = r"C:\Users\fkmic\Downloads\flappybird.png"
bird = pygame.image.load(image)
scale_x = SCALE_FACTOR * HEIGHT
scale_y = SCALE_FACTOR * WIDTH
scaled_image = pygame.transform.scale(bird, (scale_x, scale_y))
bird_controls = bird.get_rect()

while(running == True):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False


    keys = pygame.key.get_pressed()
    if(keys[pygame.K_LEFT]):
        bird_controls.x -= VELOCITY
    if(keys[pygame.K_RIGHT]):
        bird_controls.x += VELOCITY
    if(keys[pygame.K_UP]):
        bird_controls.y -= VELOCITY
    if(keys[pygame.K_DOWN]):
        bird_controls.y += VELOCITY

    if(bird_controls.left > 0):
        bird_controls.left = 0
    if(bird_controls.left > HEIGHT):
        bird_controls.left = HEIGHT
    screen.fill((0,0,0))
    screen.blit(scaled_image, bird_controls)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()