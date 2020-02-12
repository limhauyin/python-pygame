import pygame 
import random 
import math
# init game
pygame.init()

# height and weight
screen = pygame.display.set_mode((800,600))

# title and icon 
pygame.display.set_caption("Killer")
icon = pygame.image.load('tuna.png')
pygame.display.set_icon(icon)

# background 
background = pygame.image.load('wenyibackground.jpeg')

# player
playerIMG = pygame.image.load('fisher.png')
playerX = 370
playerY = 480
playerX_change = 0 
playerY_change = 0 



# enemy
enemyIMG = pygame.image.load('wenyi.jpeg')
enemyX = random.randint(0,800)
enemyY = random.randint(40,150)
enemyX_change = 4
enemyY_change = 10 

# bullet
# ready = not moving
# fire = moving
bulletIMG = pygame.image.load('swear.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

score = 0 
def player(x,y):
    screen.blit(playerIMG,(x,y))

def enemy(x,y):
    screen.blit(enemyIMG,(x,y))

def fire_bullet(x,y):
    global bullet_state 
    bullet_state = "fire"
    screen.blit(bulletIMG,(x,y))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX,2)) + (math.pow(enemyY- bulletY,2)))
    if(distance<27):
        return True
    else :
        return False

# game loop
running = True
while running : 
    #RGB  
    screen.fill((255,255,255))
    # back ground 
    # screen.blit(background,(0,0))
    for event in pygame.event.get() : 
        if(event.type == pygame.QUIT) :
            running = False
    
        # check key is press 
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_LEFT):
                playerX_change = -5
            if(event.key == pygame.K_RIGHT):
                playerX_change = 5
            if(event.key == pygame.K_SPACE):
                if(bullet_state == "ready"):
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)


        if(event.type == pygame.KEYUP):
            if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                playerX_change = 0


        
    playerX += playerX_change
    if(playerX >= 765):
        playerX = 765
    elif(playerX <= 0):
        playerX = 0

    # eneny movment 
    enemyX += enemyX_change
    if(enemyX >= 765):
        enemyX_change = -4
        enemyY += enemyY_change
    elif(enemyX <= 0):
        enemyX_change = 4
        enemyY -= enemyY_change

    # BUllet momement 

    if(bulletY <= 0):
        bulletY = 480
        bullet_state ="ready"

    if(bullet_state == "fire"):
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    #Collision
    collision = isCollision(enemyX,enemyY,bulletX,bulletY)

    if(collision):
        bulletY = 480
        bullet_state = "ready"
        score += 1


    player(playerX,playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
