# Import pygame library
import pygame

# Initialize pygame
pygame.init()

# Create the game window/screen
screen = pygame.display.set_mode((400,600))

# Create a rectangle for paddle object
paddle = pygame.Rect(200,500,30,10)

# Create a rectangle for ball object
ball = pygame.Rect(70,50,10,10)

# Game loop
while True:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    # Draw blue colored paddle on screen
    pygame.draw.rect(screen,(23,100,100),paddle)
    
    # Draw a white colored ball on screen
    pygame.draw.rect(screen,(255,255,255),ball)
    
    # Update the display with paddle and ball objects
    pygame.display.update()
