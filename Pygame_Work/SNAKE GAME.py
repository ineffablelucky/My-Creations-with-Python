# Snake Game
# my first game

# imports
import pygame, sys, random, time
pygame.init() # for displaying fonts(i solved my font error with this line)

# Player Surface
playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption("Snake Game!")

# Color((r,g,b))
red = pygame.Color(250, 0, 0)  # game over
green = pygame.Color(0, 255, 0)  # snake
black = pygame.Color(0, 0, 0)  # Score
orange = pygame.Color(255, 165, 0)  # background
brown = pygame.Color(165, 42, 42)  # food

# FPS control
fpsController = pygame.time.Clock()

# Important variable
snakePos = [100, 50]  # first snake pos
snakeBody = [[100, 50], [90, 50], [80, 50]]  # snake body Position

foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]  # first food position
foodSpawn = True

direction = "Right"  # first direction
changeto = direction

score = 0

# GameOver Function
def gameOver():
    myFont = pygame.font.SysFont("monaco", 72)  # using system font
    onSurface = myFont.render('Game Over!', True, red)  # display game over on the screen/console
    GOrect = onSurface.get_rect()  # Rectangular components are x and y. Gorect is used because i want to draw inside the rectangle, and also blit()  requires it.
    GOrect.midtop = (360, 15)  # positioning the TExt
    playSurface.blit(onSurface, GOrect)
    showScore(0)
    pygame.display.flip()  # updates the screen; REALLY IMPORTANT CODE
    time.sleep(4)
    pygame.quit()  # pygame exit
    sys.exit()  # console exit

# for score card
def showScore(choice=1):
    sFont = pygame.font.SysFont('monaco', 24)
    Ssurf = sFont.render('Score : {0}'.format(score), True, black)
    Srect = Ssurf.get_rect()
    if choice == 1:
        Srect.midtop = (80, 10)
    else:
        Srect.midtop = (360, 120)
    playSurface.blit(Ssurf, Srect)


# Main Logic of the Game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # for quitting the game, QUIT denotes red X on side of the window to close
            pygame.quit()  # this uninitialize all pygame modules. this does not actually exit the program
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # KEYDOWN for when key is kept pressed and not release
            # here i am marking keys for movements of snake. up,down right and left arrow.
            if event.key == pygame.K_RIGHT or event.key == ord('d'):  # K_right denotes right arrow key
                changeto = "Right"  # direction changed to right
            elif event.key == pygame.K_LEFT or event.key == ord('a'): # "ord()" will give ascii value of aphlabets
                changeto = "Left"
            elif event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = "Down"
            elif event.key == pygame.K_UP or event.key == ord('w'):
                changeto = "Up"

            elif event.key == pygame.K_ESCAPE:  # if you press escape to quit
                pygame.event.post(pygame.event.Event(pygame.QUIT))  # post() is when we create an event

    # validation of direction# move the snake in right direction
    if changeto == "Right" and not direction == "Left":
        direction = "Right"
    elif changeto == "Up" and not direction == "Down":
        direction = "Up"
    elif changeto == "Left" and not direction == "Right":
        direction = "Left"
    elif changeto == "Down" and not direction == "Up":
        direction = "Down"

    # update snake position
    if direction == "Right":
        snakePos[0] += 10
    elif direction == "Up":
        snakePos[1] -= 10
    elif direction == "Down":
        snakePos[1] += 10
    elif direction == "Left":
        snakePos[0] -= 10

    # Snake Body
    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:  # it means snake touches the egg
        score += 1
        foodSpawn = False
    else:
        snakeBody.pop()

    if foodSpawn == False:  # regenerate the egg
        foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]

    foodSpawn = True

    # Drawing Part

    playSurface.fill(orange)  # to change the background white
    for pos in snakeBody:  # to continuously update snake position and draw on screen
        pygame.draw.rect(playSurface, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0], foodPos[1], 10, 10))  # to draw egg

    if snakePos[0] > 710 or snakePos[0] < 0:  # to set boundaries for snake so that he doesn't go out of window
        gameOver()
    elif snakePos[1] > 450 or snakePos[1] < 0:
        gameOver()

    # for snake touching itself
    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver()

    showScore()
    pygame.display.flip()  # to update the window
    fpsController.tick(15)  # to limit the speed of snake
