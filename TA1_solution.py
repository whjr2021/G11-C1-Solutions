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
            
    
