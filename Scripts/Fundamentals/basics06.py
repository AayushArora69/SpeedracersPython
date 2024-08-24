import pygame
pygame.init()

HEIGHT = 1280
WIDTH = 720
SPEED = 30

screen = pygame.display.set_mode((HEIGHT, WIDTH))
caption = pygame.display.set_caption("Movement")
image_to_load = r"C:\Users\fkmic\Downloads\adhee cameo.png"
image = pygame.image.load(image_to_load)
scale_factor = 0.4
new_scaled_height_of_image = (HEIGHT * scale_factor)
new_scaled_width_of_image = (WIDTH * scale_factor)
scaled_image = pygame.transform.scale(image, (new_scaled_height_of_image, new_scaled_width_of_image))
rect_of_image = scaled_image.get_rect()
rect_of_image.x = WIDTH//2
rect_of_image.y = HEIGHT//8
red = (255,0,0)
blue = (0,0,255)

running = True
while(running == True):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False

        if i.type == pygame.KEYDOWN:
            if (i.key == pygame.K_LEFT):
                rect_of_image.x -= SPEED
            if(i.key == pygame.K_RIGHT):
                rect_of_image.x += SPEED
            if(i.key == pygame.K_DOWN):
                rect_of_image.y += SPEED
            if(i.key == pygame.K_UP):
                rect_of_image.y -= SPEED
        screen.fill((0,0,0))
        screen.fill(red)
        screen.blit(scaled_image, rect_of_image)
        pygame.display.update()
pygame.quit()