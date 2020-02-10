import pygame 

# init game
pygame.init()

# height and weight
screen = pygame.display.set_mode((800,600))

# title and icon 
pygame.display.set_caption("Killer")
icon = pygame.image.load('fish.png')
pygame.display.set_icon(icon)


# player
playerIMG = pygame.image.load('fisher.png')
playerX = 370
playerY = 480
playerX_change = 0 
playerY_change = 0 



# enemy
enemyIMG = pygame.image.load('tuna.png')
enemyX = 370
enemyY = 180
enemyX_change = 0 
enemyY_change = 0 


def player(x,y):
    screen.blit(playerIMG,(x,y))

def enemy(x,y):
    screen.blit(enemyIMG,(x,y))
# game loop
running = True
while running : 
    #RGB  
    screen.fill((0,0,0))
    for event in pygame.event.get() : 
        if(event.type == pygame.QUIT) :
            running = False
    
        # check key is press 
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_LEFT):
                playerX_change = -0.3
            if(event.key == pygame.K_RIGHT):
                playerX_change = 0.3
        if(event.type == pygame.KEYUP):
            if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                playerX_change = 0
    
    playerX += playerX_change
    if(playerX >= 765):
        playerX = 765
    elif(playerX <= 0):
        playerX = 0

    player(playerX,playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
