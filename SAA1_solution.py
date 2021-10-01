# Import pygame library
import pygame

# Initialize pygame
pygame.init()

# Create the game window/screen
screen = pygame.display.set_mode((400,600))

# Create a rectangle for paddle object
paddle = pygame.Rect(200,500,100,30)

# Create a rectangle for ball object 
ball = pygame.Rect(70,50,20,20)

# Game loop
while True:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    # Draw a golden colored paddle on screen
    pygame.draw.rect(screen,(218,165,32),paddle)
    
    # Draw an orange colored ball on screen
    pygame.draw.rect(screen,(255,69,0),ball)
    
    # Update the display with paddle and ball objects
    pygame.display.update()