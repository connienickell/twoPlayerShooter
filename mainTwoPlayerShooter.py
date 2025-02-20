import pygame
import os
import time
import random
pygame.init()

clock = pygame.time.Clock()
fps = 60

WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Player Shooter")

#player placement
playerOneX = 20
playerOneY = HEIGHT/2

playerTwoX = WIDTH - 30
playerTwoY = HEIGHT/2 - 10

#arrays of lasers
playerOneLasers = []
playerTwoLasers = []

laserVelX = 10

#players' health
playerOneHealth = 3
playerTwoHealth = 3

#detect collisions
# def collisionPlayerOne():
#     for laser in playerOneLasers:
#         if playerTwoCoordinates touch laser coordinates
#         playerTwoHealth -= 1 

# def collisionPlayerTwo():
#     for laser in playerOneLasers:
#         if playerTwoCoordinates touch laser coordinates
#         playerTwoHealth -= 1 


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
        if not playerOneX > WIDTH/2 - 10:
            playerOneX += 3
    if key_pressed [pygame.K_LSHIFT]:
            createAndAppendLasersPlayerOne()

    if key_pressed [pygame.K_LEFT]:
        global playerTwoX
        if not playerTwoX < WIDTH/2 + 10:
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

playerOneCoolDown = 0
playerTwoCoolDown = 0

def createAndAppendLasersPlayerOne():
    global playerOneCoolDown
    if playerOneCoolDown <= 0:
        playerOneLasers.append([playerOneX + 14, playerOneY - 3])
        playerOneCoolDown = 25
    
def createAndAppendLasersPlayerTwo():
    global playerTwoCoolDown
    if playerTwoCoolDown <= 0:
        playerTwoLasers.append([playerTwoX - 20, playerTwoY + 9])
        playerTwoCoolDown = 25


#                #
# main game loop #
#                #
running = True
while running:
    # Leave the loop if player quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    handleUserInput()

    screen.fill((0, 0, 0))
    
    # draw players
    playerOne = pygame.draw.circle(screen, (245, 40, 40), (playerOneX, playerOneY), 10)
    playerTwo = pygame.draw.rect(screen, (40, 40, 245), pygame.Rect(playerTwoX, playerTwoY, 20, 20), 10)

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

