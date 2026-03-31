import pygame
import sys
import random
import time

# 1. Initialize Pygame
pygame.init()

# 2. Define window dimensions
WIDTH = 1000
HEIGHT = 1000
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

square_rect = pygame.Rect(offsetX-20, newHeight-70, 550, 550)

pygame.draw.rect(screen, blackSquares, square_rect)
pygame.display.flip()

square_rect = pygame.Rect(offsetX-10, newHeight-60, 520, 520)

pygame.draw.rect(screen, background_colour, square_rect)
pygame.display.flip()

#if colorBool = false, color is white, else black
colorBool = False
squareLists = []



# 2. Create a Font object (once, outside the loop)
# Use the default system font at size 36
font = pygame.font.SysFont(pygame.font.get_default_font(), 36)

# 3. Render the text surface (once, or when text changes)
text_surface = font.render("Hello World", True, (255,0,0))

# 4. Get the text rectangle and set its position
text_rect = text_surface.get_rect()
text_rect.center = (WIDTH//2+50, 400)

square_rect = pygame.Rect(WIDTH // 2 - 36, 360, individualHeight, individualWidth)
pygame.draw.rect(screen, (128, 128, 128), square_rect)

rows = ["1", "2","3","4","5","6","7","8"]
columns = ["a","b","c","d","e","f","g","h"]

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

def generateRandomCoord():
    row = random.randint(0,len(rows)-1)
    col = random.randint(0, len(columns)-1)
    print(row)
    print(col)

    
    return [row,col]
#pass in a list of [row,col]
def getCoordName(box):
    rowName = rows[box[0]]
    colName = columns[box[1]]
    return colName + rowName

def getSquareFromCoord(box):
    index = 8 * (box[0])
    index += box[1]
    return index
print("spacer")
holder = generateRandomCoord()



#holder = [5,0] 
#holder[0] -= 1
#holder[1] -= 1
print(getCoordName(holder))
print(getSquareFromCoord(holder))

#Stages:

#Stage one, start game

#Stage two, generate the random places

#Stage three, detect user button press and loop back

#Ideas: use two while loops, one for when the game is not started yet, one for when the game is running

#Use a variable to switch between while loops
print("spacy")
print(squareLists)
print("spice")

gameMode = False
needNewCoordinate = False
clickedSquare = ""

rows = rows[::-1]
columns = columns

#These will be the points:

goodPoints = 0
badPoints = 0

decisionWasMade = False

while running:
    # 6. Event handling
    #print("test")
    #print(squareLists)
    screen.fill(background_colour)
    square_rect = pygame.Rect(WIDTH // 2 - 36, 360, individualHeight, individualWidth)
    pygame.draw.rect(screen, (128, 128, 128), square_rect)


    
    offsetX = newWidth/2
    currentCoords = [offsetX,newHeight-50]

    
    
    square_rect = pygame.Rect(offsetX-20, newHeight-70, 550, 550)
    

    pygame.draw.rect(screen, blackSquares, square_rect)
    

    square_rect = pygame.Rect(offsetX-10, newHeight-60, 520, 520)

    play_again_rect = pygame.Rect(WIDTH // 2 - 100, 150, 200, 50)

    pygame.draw.rect(screen, background_colour, square_rect)
    for i,square in enumerate(squareLists):
        squareObj = square[0]
        whiteOrBlack = square[1]
        if(whiteOrBlack == False):
            current_color = background_colour
        else:
            current_color = blackSquares
        pygame.draw.rect(screen, current_color, squareObj)
    #pygame.display.flip()
        

    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Check if the user clicked the close button
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
                # The left mouse button is event.button == 1
                
                if event.button == 1:
                    if(gameMode == True):
                        # Check if the mouse position (event.pos) is inside the box
                        mouse_pos = pygame.mouse.get_pos()
                        for i,square in enumerate(squareLists):
                            # 2. Check if the mouse position collides with the box's Rect
                            print(mouse_pos)
                            squareObj = square[0]
                            
                            if squareObj.collidepoint(mouse_pos):
                                squareObj = square[0]
                                whiteOrBlack = square[1]
                                
                                clickedSquare = squareObj
                                
                                
                                #exit()
                                #current_color = (0, 0, 255)
                    else:
                        mouse_pos = pygame.mouse.get_pos()
                        if(play_again_rect.collidepoint(mouse_pos)):
                            clickedSquare = play_again_rect
                            print("testu")
                            print(clickedSquare)
                            #exit()
             

    #While loop for starting

    if(gameMode == False):
        coordName = ""
        
        needNewCoordinate = True
        #gameMode = True
        goodPoints = 0
        badPoints = 0

        #play_again_rect = pygame.Rect(WIDTH // 2 - 50, 100, 200, 200)
        pygame.draw.rect(screen, (128, 128, 128), play_again_rect)
        targetCoord = play_again_rect
        text_surface = font.render("Play again?", True, (255,0,0))

        screen.blit(text_surface, play_again_rect)
        pygame.display.flip()
        #print('test')
        #print(clickedSquare)
        if(clickedSquare != ""):
            print("agh")
            print(clickedSquare)
            print(targetCoord)
            #exit()
        if(clickedSquare == targetCoord):
            print("chiky")
            #exit()
            targetCoord = ""
            gameMode = True


    text_surface = font.render(coordName, True, (255,0,0))
    screen.blit(text_surface, text_rect)

    #While loop for playing
    if(gameMode == True):

        if(goodPoints >= 6):
            new_text_rect = text_surface.get_rect()
            new_text_rect.center = (WIDTH//2, 300)

            square_rect = pygame.Rect(WIDTH // 2 - 36, 360, individualHeight, individualWidth)
            pygame.draw.rect(screen, (128, 128, 128), square_rect)
            text_surface = font.render("You win!", True, (0,255,0))
            screen.blit(text_surface, new_text_rect)
            pygame.display.flip()
            time.sleep(1)
            gameMode = False
            
        if(badPoints >= 6):
            new_text_rect = text_surface.get_rect()
            new_text_rect.center = (WIDTH//2, 300)

            square_rect = pygame.Rect(WIDTH // 2 - 36, 360, individualHeight, individualWidth)
            pygame.draw.rect(screen, (128, 128, 128), square_rect)
            text_surface = font.render("You Lose", True, (255,0,0))
            screen.blit(text_surface, new_text_rect)
            pygame.display.flip()
            time.sleep(1)
            gameMode = False
            
            
        

        for i in range(6):
            if(i < goodPoints):
                pygame.draw.circle(screen, (0,255,0), (100+(i*110), 100), 50, 0)
            else:
                pygame.draw.circle(screen, (0,255,0), (100+(i*110), 100), 50, 5)

        for i in range(6):
            if(i < badPoints):
                pygame.draw.circle(screen, (255,0,0), (100+(i*110), 200), 50, 0)
            else:
                pygame.draw.circle(screen, (255,0,0), (100+(i*110), 200), 50, 5)
        if(needNewCoordinate == True):
            #generate a new coordinate
            holder = generateRandomCoord()
            #holder = [0,0]
            coordName = getCoordName(holder)
            boxIndex = getSquareFromCoord(holder)
            targetCoord = squareLists[boxIndex]

            needNewCoordinate = False
        mouse_pos = pygame.mouse.get_pos() #
        
        for i,square in enumerate(squareLists):
            
            squareObj = square[0]
            whiteOrBlack = square[1]
            if(whiteOrBlack == False):
                current_color = background_colour
            else:
                current_color = blackSquares
            pygame.draw.rect(screen, current_color, squareObj)
        
        for i,square in enumerate(squareLists):
            # 2. Check if the mouse position collides with the box's Rect
            squareObj = square[0]
            whiteOrBlack = square[1]
            
            if(squareObj == clickedSquare):
                
                if(clickedSquare != targetCoord[0]):
                    current_color = (255,0,0)
                    badPoints += 1

                else:
                    current_color = (0,255,0)
                    goodPoints += 1
                
                    needNewCoordinate = True
                decisionWasMade = True
            
            elif(squareObj.collidepoint(mouse_pos)):
                
                current_color = (255, 165, 0)
            else:
                if(whiteOrBlack == False):
                    current_color = background_colour
                else:
                    current_color = blackSquares
        
            #screen.fill(background_colour)
            pygame.draw.rect(screen, current_color, squareObj)
            if(decisionWasMade == True):
                pygame.display.flip()
                print(current_color)
                print("space")
                print(targetCoord)
                print(clickedSquare)
                #pygame.draw.rect(screen, (0,255,0), targetCoord[0])
                #pygame.display.flip()
                time.sleep(0.25)
                clickedSquare = ""
                decisionWasMade = False
                break
            

        pygame.display.flip()

        # 7. Update the display (this is done in each loop iteration for animations)
        # pygame.display.update() or pygame.display.flip()

# 8. Quit Pygame once the loop ends
pygame.quit()
sys.exit()
