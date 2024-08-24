import pygame

pygame.init()

# Constants
HEIGHT = 1280
WIDTH = 720
RED = (255, 0, 0)

# Initialize screen
surface = pygame.display.set_mode((HEIGHT, WIDTH))  # Corrected order: width, height
pygame.display.set_caption("Sounds!")

# Load sounds
sound_1 = pygame.mixer.Sound("jump.mp3")
sound_2 = pygame.mixer.Sound("funnyjump.mp3")

# Play sounds
sound_1.play()
pygame.time.delay(1500)  # Wait 1500ms before playing the second sound
sound_2.play()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen with red
    surface.fill(RED)
    
    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()
