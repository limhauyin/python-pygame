import pygame 
import random 
import math
from pygame import mixer

# init game
pygame.init()

# height and weight
screen = pygame.display.set_mode((800,600))

# title and icon 
pygame.display.set_caption("Kill Demon")
icon = pygame.image.load('wy2.png')
pygame.display.set_icon(icon)

# background 
background = pygame.image.load('wy3.jpg')


#music
mixer.music.load('game.mp3')
mixer.music.play(-1)

# player
playerIMG = pygame.image.load('war.png')
playerX = 370
playerY = 530
playerX_change = 0 
playerY_change = 0 



# enemy
enemyIMG = []
enemyX = []
enemyY = []
enemyX_change =[]
enemyY_change = []
enemy_num = 2 

for i in range(enemy_num):
    enemyIMG.append(pygame.image.load('wy6.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(20,150))
    enemyX_change.append(4)
    enemyY_change.append(10) 

# bullet
# ready = not moving
# fire = moving
bulletIMG = pygame.image.load('poop.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 40
bullet_state = "ready"

score_value = 0 
font = pygame.font.Font('freesansbold.ttf',20)
overfont = pygame.font.Font('freesansbold.ttf', 64)

textX = 10 
textY = 10 

def show_score(x,y):
    score= font.render(str(score_value) + " Wen Yi is Killed !", True, (0,0,0))
    screen.blit(score,(x,y))

def player(x,y):
    screen.blit(playerIMG,(x,y))

def enemy(x,y,i):
    screen.blit(enemyIMG[i],(x,y))

def fire_bullet(x,y):
    global bullet_state 
    bullet_state = "fire"
    screen.blit(bulletIMG,(x+15,y))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX,2)) + (math.pow(enemyY- bulletY,2)))
    if(distance<50):
        return True
    else :
        return False


def  game_over_text():
    score= font.render("You are killed by Wen Yi", True, (255,255,255))
    screen.blit(score,(200,250))
    sound = mixer.Sound('lose1.ogg')
    sound.play()


# game loop
running = True
while running : 
    #RGB  
    screen.fill((255,255,255))
    # back ground 
    screen.blit(background,(0,0))
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
                    sound = mixer.Sound('gun1.ogg')
                    sound.play()


        if(event.type == pygame.KEYUP):
            if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                playerX_change = 0


        
    playerX += playerX_change
    if(playerX >= 765):
        playerX = 765
    elif(playerX <= 0):
        playerX = 0

    for i in range(enemy_num):
        #game over 
        if(enemyY[i] > 440):
            for j in range(enemy_num):
                enemyY[j] = 2000
            game_over_text()
            break


        # eneny movment 
        enemyX[i] += enemyX_change[i]
        if(enemyX[i] >= 765):
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]
        elif(enemyX[i] <= 0):
            enemyX_change[i] = 4
            enemyY[i] -= enemyY_change[i]
        #Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)

        if(collision):
            bulletY = 480
            dead_sound = mixer.Sound('fart1.ogg')
            dead_sound.play()
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(20, 150)
        
        enemy(enemyX[i], enemyY[i], i)

    # BUllet momement 

    if(bulletY <= 0):
        bulletY = 480
        bullet_state ="ready"

    if(bullet_state == "fire"):
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change


    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()
