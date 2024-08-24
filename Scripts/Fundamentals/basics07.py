import pygame
pygame.init()
HEIGHT = 1280
WIDTH = 720
running = True
image = r"C:\Users\fkmic\Downloads\channels4_profile.jpg"
screen = pygame.display.set_mode((HEIGHT, WIDTH))
caption = pygame.display.set_caption("Mouse Movement")
flapz = pygame.image.load(image)
rect_image = flapz.get_rect()
rect_image.x = 10
rect_image.y = 15

while(running == True):
    for action in pygame.event.get():
        print(action)
        if (action.type == pygame.QUIT):
            running = False
        if(action.type == pygame.MOUSEBUTTONDOWN):
            new_position_x = action.pos[0]
            new_position_y = action.pos[1]
            rect_image.centerx = new_position_x
            rect_image.centery = new_position_y
        if(action.type == pygame.MOUSEMOTION and action.buttons[2] == 1): #It ensures that we are able to move the sprite only if we are clicking
            new_position_x = action.pos[0]
            new_position_y = action.pos[1]
            rect_image.centerx = new_position_x
            rect_image.centery = new_position_y

        screen.fill((0,0,0))
        screen.blit(flapz, rect_image)
        pygame.display.update()
pygame.quit()