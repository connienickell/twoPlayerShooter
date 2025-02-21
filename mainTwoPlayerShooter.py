import pygame
import os
import time
import random
import startButton
pygame.init()

clock = pygame.time.Clock()
fps = 60

WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Player Shooter")

#load button images
startImg = pygame.image.load(os.path.join('assets', 'start_button.png')).convert_alpha()

playerOneCoolDown = 0
playerTwoCoolDown = 0
    
#create button instances
startButton = startButton.Button(300, 280, startImg, 0.2)

#player placement
playerOneX = 20
playerOneY = HEIGHT/2
playerOneX2 = playerOneX + 25
playerOneY2 = playerOneY + 25

playerTwoX = WIDTH - 35
playerTwoY = HEIGHT/2
playerTwoX2 = playerTwoX + 25
playerTwoY2 = playerTwoY + 25

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

    pygame.display.update()
    
    #update player cooldown corresponding with fps
    playerOneCoolDown -= 1
    playerTwoCoolDown -= 1

    #check for winner
    if playerOneHealth == 0:
        print("player two wins!")
        pygame.time.delay(2000)
        pygame.quit()

    if playerTwoHealth == 0:
        print("player one wins!")
        pygame.time.delay(2000)
        pygame.quit()

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

