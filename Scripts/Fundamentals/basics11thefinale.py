import pygame
import random

pygame.init()
HEIGHT = 1280 #x
WIDTH = 720 #y
fps = 15
SCALE_FACTOR = 0.2
SCALE_FACTOR_COIN = 0.3
REDUCED_HEIGHT_VALUE = 15
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((HEIGHT, WIDTH))
caption = pygame.display.set_caption("Collision Detection!")
CURRENT_SCORE = 0
sys_font = pygame.font.SysFont("Calibri", 64)

SPEED = 10
#Load images
image = r"C:\Users\fkmic\Downloads\adhee cameo.png"
bird = pygame.image.load(image)
scale_x = SCALE_FACTOR * HEIGHT
scale_y = SCALE_FACTOR * WIDTH
scaled_image = pygame.transform.scale(bird, (scale_x, scale_y))
bird_controls = scaled_image.get_rect()
bird_controls.height -= REDUCED_HEIGHT_VALUE - 10
bird_controls.width -= REDUCED_HEIGHT_VALUE + 5

scale_coin_x = SCALE_FACTOR_COIN * HEIGHT
scale_coin_y = SCALE_FACTOR_COIN * WIDTH
coin_sprite = pygame.image.load(r"C:\Users\fkmic\OneDrive\Desktop\Pixel Art\Coin.png")
scaled_image_coin = pygame.transform.scale(coin_sprite, (125, 155))
coin_rect = scaled_image_coin.get_rect()
coin_rect.x = 350
coin_rect.y = 265
running = True

while(running):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
    key = pygame.key.get_pressed()

    if(key[pygame.K_w]) and bird_controls.top > 0:
        bird_controls.y -= SPEED
    if(key[pygame.K_s]) and bird_controls.top < 660:
        bird_controls.y += SPEED
    if(key[pygame.K_a]) and bird_controls.left > 0:
        bird_controls.x -= SPEED
    if(key[pygame.K_d]) and bird_controls.right < 1770:
        bird_controls.x += SPEED

    if(bird_controls.colliderect(coin_rect)):
        CURRENT_SCORE += 1

        print('collision detected sir!')
        coin_rect.left = random.randint(0, HEIGHT)
        coin_rect.top = random.randint(0, WIDTH)
    score_font = sys_font.render(f"Score: {CURRENT_SCORE}", True, (0, 0, 255))

    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,0,0), coin_rect, 1)
    pygame.draw.rect(screen, (255,0,0), bird_controls, 1)
    screen.blit(scaled_image, bird_controls)
    screen.blit(scaled_image_coin, coin_rect)
    screen.blit(score_font, (0,0))
    CLOCK.tick(fps)
    pygame.display.update()
pygame.quit()