# Import pygame library
import pygame

# Initialize pygame
pygame.init()

# Create the game window/screen
screen = pygame.display.set_mode((400,600))

# Create a rectangle for paddle object
paddle = pygame.Rect(200,500,30,10)

# Game loop
while True:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    # Draw blue colored paddle on screen
    pygame.draw.rect(screen,(23,100,100),paddle)
    
    # Update the display with paddle object
    pygame.display.update()

