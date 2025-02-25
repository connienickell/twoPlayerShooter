import pygame
import os
import time
import startButton
import utilities
pygame.init()

clock = pygame.time.Clock()
fps = 60

WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Player Shooter")

#load button images
startImg = pygame.image.load(os.path.join('assets', 'start_button.png')).convert_alpha()

#laser timing
playerOneCoolDown = 0
playerTwoCoolDown = 0
    
#create button instances
startButton = startButton.Button(300, 280, startImg, 0.2)

#player coordinates
playerOneX = 20
playerOneY = HEIGHT/2
playerTwoX = WIDTH - 35
playerTwoY = HEIGHT/2

playerWidth = 25
playerHeight = 25

#arrays of players' lasers
playerOneLasers = []
playerTwoLasers = []

laserVelX = 10

#players' health
playerOneHealth = 3
playerTwoHealth = 3

#player one = awsd and L shift
#player two = d,r,l,u and m
#handle input/move players
def handleUserInput():
    key_pressed = pygame.key.get_pressed()
    if key_pressed [pygame.K_a]:
        global playerOneX
        if not playerOneX < 0:
            playerOneX -= 3
    if key_pressed [pygame.K_w]:
        global playerOneY
        if not playerOneY < 0:
            playerOneY -= 3
    if key_pressed [pygame.K_s]:
        if not playerOneY > HEIGHT:
            playerOneY += 3
    if key_pressed [pygame.K_d]:
        if not playerOneX > WIDTH/2 - 20:
            playerOneX += 3
    if key_pressed [pygame.K_LSHIFT]:
        createAndAppendLasersPlayerOne()

    if key_pressed [pygame.K_LEFT]:
        global playerTwoX
        if not playerTwoX < WIDTH/2 + 20:
            playerTwoX -= 3
    if key_pressed [pygame.K_UP]:
        global playerTwoY
        if not playerTwoY < 0 - 5: 
            playerTwoY -= 3
    if key_pressed [pygame.K_DOWN]:
        if not playerTwoY > HEIGHT - 5:
            playerTwoY += 3
    if key_pressed [pygame.K_RIGHT]:
        if not playerTwoX > WIDTH - 10:
            playerTwoX += 3
    if key_pressed [pygame.K_m]:
        createAndAppendLasersPlayerTwo()

def createAndAppendLasersPlayerOne():
    global playerOneCoolDown
    if playerOneCoolDown <= 0:
        playerOneLasers.append([playerOneX + 23, playerOneY + 10])
        playerOneCoolDown = 25
    
def createAndAppendLasersPlayerTwo():
    global playerTwoCoolDown
    if playerTwoCoolDown <= 0:
        playerTwoLasers.append([playerTwoX - 18, playerTwoY + 12])
        playerTwoCoolDown = 25

#collision control
def detectCollisionPlayerOne():
    global playerOneHealth
    for laser in playerTwoLasers[:]:
        # print("laser x =" + str(laser[0]) + ": player one right side" + str(playerOneX2)) 
        if (playerOneX + playerWidth < laser[0]) or (playerOneX > laser[0] + 15):
            # print ("outside x bounds")
            continue
        elif (playerOneY > laser[1] + 5) or (playerOneY + playerHeight < laser[1]):
            # print("outside y bounds")
            continue
        else:
            playerTwoLasers.remove(laser)
            playerOneHealth -= 1

def detectCollisionPlayerTwo():
    global playerTwoHealth
    for laser in playerOneLasers[:]:
        if (playerTwoX > laser[0] + 15) or (playerTwoX + playerWidth < laser[0]): 
            continue
        elif (playerTwoY > laser[1] + 5) or (playerTwoY + playerHeight < laser[1]):
            continue
        else:
            playerOneLasers.remove(laser)
            playerTwoHealth -= 1


running = False
startup = True

#            #
# start page #
#            #

while startup:
    screen.fill((4, 20, 40))

    if startButton.draw(screen):
        running = True
        startup = False

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            startup = False




#                #
# main game loop #
#                #

while running:
    # Leave the loop if player quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    handleUserInput()

    screen.fill((4, 20, 40))
    
    # draw players
    playerOne = pygame.draw.rect(screen, (253, 253, 150), (playerOneX, playerOneY, 25, 25), 8)
    playerTwo = pygame.draw.rect(screen, (169, 198, 227), pygame.Rect(playerTwoX, playerTwoY, 25, 25), 8)

    #draw and move lasers
    for laser in playerOneLasers:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(laser[0], laser[1], 15, 5), 8)
        laser[0] += laserVelX

    for laser in playerTwoLasers: 
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(laser[0], laser[1], 15, 5), 8)
        laser[0] -= laserVelX

    detectCollisionPlayerOne()
    detectCollisionPlayerTwo()

    pygame.display.update()
    
    #update player cooldown corresponding with fps
    playerOneCoolDown -= 1
    playerTwoCoolDown -= 1

    #check for winner
    if playerOneHealth == 0:
        print("player two wins!")
        pygame.time.delay(2000)
        startup = True
        running = False

    if playerTwoHealth == 0:
        print("player one wins!")
        pygame.time.delay(2000)
        startup = True
        running = False

    clock.tick(fps)

pygame.quit()

# be able to shoot at each other
    # controls: aswd + 1(shoot) and up, down, l, r + m(shoot)
        # cannot cross midline DONE
        # shooting cooldown DONE
# lose health when hit
    # if either player loses all health
        # display winner
# start screen 

# I am grateful for basecamp, such a good bright atmosphere to work in
# I am grateful for changing seasons - it's so mesmerizing to see the new buds pop up and the outdoor activities spring up
# I am grateful for art- some of it I'll never understand the appeal of, but the rest of it inspires me to find the creative parts of my brain
# I am grateful for coffee. Yes, it may be my addiction, but it is also what many conversations have centered around
# I am grateful for family. My biological family shows me what I am missing, and the family I choose surprises me with what family can be
# I am grateful 