import pygame
import sys
import random

# 1. Initialize Pygame
pygame.init()

# 2. Define window dimensions
WIDTH = 800
HEIGHT = 800
SQUARE_COLOR = (255, 0, 0) 
#space for the chess board: newWidth = width/2 and newHeight = height/2, space for each square is newHeight/8, and newWidth/8
newWidth = WIDTH/2
newHeight = HEIGHT/2

individualWidth = newWidth/8
individualHeight = newHeight/8

print(individualWidth)
print(individualHeight)

# Create the display surface (window)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# 3. Set the window title
pygame.display.set_caption("My Pygame Window")

# 4. Set the background color (RGB values) and fill the screen
background_colour = (255, 255, 255) # White
blackSquares = (0,0,0)
screen.fill(background_colour)
pygame.display.flip() # Update the full display to the screen
offsetX = newWidth/2
currentCoords = [offsetX,newHeight-50]

square_rect = pygame.Rect(offsetX-20, newHeight-70, 450, 450)

pygame.draw.rect(screen, blackSquares, square_rect)
pygame.display.flip()

square_rect = pygame.Rect(offsetX-10, newHeight-60, 420, 420)

pygame.draw.rect(screen, background_colour, square_rect)
pygame.display.flip()

#if colorBool = false, color is white, else black
colorBool = False
squareLists = []

for i in range(8):
    for j in range(8):
        square_rect = pygame.Rect(currentCoords[0], currentCoords[1], individualHeight, individualWidth)
        # Other game logic and drawing can go here
        if(colorBool == False):    
            pygame.draw.rect(screen, background_colour, square_rect)
        else:
            pygame.draw.rect(screen, blackSquares, square_rect)
        squareLists.append([square_rect, colorBool])
        colorBool = not (colorBool)
        currentCoords[0] += individualWidth
    currentCoords[1] += individualHeight
    currentCoords[0] = offsetX
    colorBool = not (colorBool)

# 5. The Game Loop (Keeps the window open)

running = True
#[x,y]

while running:
    # 6. Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Check if the user clicked the close button
            running = False
    mouse_pos = pygame.mouse.get_pos() #

    
    for square in squareLists:
        # 2. Check if the mouse position collides with the box's Rect
        squareObj = square[0]
        whiteOrBlack = square[1]
        if squareObj.collidepoint(mouse_pos):
            
            current_color = (255, 165, 0)
        else:
            if(whiteOrBlack == False):
                current_color = background_colour
            else:
                current_color = blackSquares
        #screen.fill(background_colour)
        pygame.draw.rect(screen, current_color, squareObj)

    pygame.display.flip()

    # 7. Update the display (this is done in each loop iteration for animations)
    # pygame.display.update() or pygame.display.flip()

# 8. Quit Pygame once the loop ends
pygame.quit()
sys.exit()
