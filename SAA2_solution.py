# Import pygame library
import pygame

# Initialize pygame
pygame.init()

# Create the game window/screen
screen = pygame.display.set_mode((400,600))

# Create a rectangle for paddle object and position it on top of paddle at its center
paddle = pygame.Rect(150,500,100,30)

# Create a rectangle for ball object
ball = pygame.Rect(190,480,20,20)

while True:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    # Draw red colored paddle on screen
    pygame.draw.rect(screen,(255,0,0),paddle)
    
    # Draw the blue colored ball on screen
    pygame.draw.rect(screen,(0,0,255),ball)
    
    # Update the display with paddle and ball objects
    pygame.display.update()