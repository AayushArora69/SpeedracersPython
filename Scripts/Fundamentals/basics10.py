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
caption = pygame.display.set_caption("Limited Movement!")
image = r"C:\Users\fkmic\Downloads\flappybird.png"
bird = pygame.image.load(image)
scale_x = SCALE_FACTOR * HEIGHT
scale_y = SCALE_FACTOR * WIDTH
scaled_image = pygame.transform.scale(bird, (scale_x, scale_y))
bird_controls = bird.get_rect()

while(running == True):
    for event in pygame.event.get():
        print(bird_controls.x)
        if(event.type == pygame.QUIT):
            running = False


    keys = pygame.key.get_pressed()
    print(bird_controls.top)
    if(keys[pygame.K_LEFT] or (keys[pygame.K_a]) and bird_controls.left > 0):
        bird_controls.x -= VELOCITY
    if(keys[pygame.K_RIGHT]) or (keys[pygame.K_d]) and bird_controls.right < 1770:
        bird_controls.x += VELOCITY
    if(keys[pygame.K_UP]) or (keys[pygame.K_w]) and bird_controls.top > 0:
        bird_controls.y -= VELOCITY
    if(keys[pygame.K_DOWN]) or (keys[pygame.K_s]) and bird_controls.top < 660:
        bird_controls.y += VELOCITY
        
    screen.fill((0,0,0))
    screen.blit(scaled_image, bird_controls)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()