#creating game using python's pygame library
import pygame , sys
import time
from pygame.locals import *

pygame.init()
width = 800
height = 400

clock = pygame.time.Clock()

#defining colors
red = (200,0,0)
green = (0,200,0)
blue = (0,0,200)
black = (0,0,0)
white = (255,255,255)
bright_green = (0,255,0)
bright_red = (255,0,0)

#defining window and title
win= pygame.display.set_mode((width , height))
pygame.display.set_caption('first game ')
man = pygame.image.load("rightman.png")
#bkgd = pygame.image.load("bkgd.png")

def enemies(enemyx, enemyy, enemyw, enemyh, color):
    pygame.draw.rect(win, color, [enemyx, enemyy, enemyw, enemyh])

def enemies_dodged(count):
    font = pygame.font.SysFont('comicsansms', 25)
    text = font.render("Score: "+str(count), True, black)
    win.blit(text,(0,0))


def crash():
    fontobj = pygame.font.Font('freesansbold.ttf',92)
    textobj = fontobj.render('Game Over', True , black  )
    textrectobj = textobj.get_rect()
    textrectobj.center = ((width/2),(height/3))
    win.blit(textobj, textrectobj)

    pygame.display.update()
    time.sleep(3)
    gameloop()

def gameloop():
    z=0
    x=width-750
    y=height-200
    vel=5
    jump = False
    jumpcount = 10

    enemy_startx = width - 53
    enemy_starty = height - 130
    enemy_speed = 7
    enemy_width = 30
    enemy_height = 30

    score = 0


 
    #main loop
    run= True
    while run:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if not(jump):
            if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                jump = True         
        else:
            if jumpcount >= -10:
                neg=1
                if jumpcount <0:
                    neg = -1  
                y -= (jumpcount ** 2) * 0.5 * neg
                jumpcount -=1

            else:
                jump = False
                jumpcount = 10

        win.fill(white)
       # win.blit(bkgd,(z,0))
        #z -= 1
        win.blit(man,(x,y))
      
        enemies(enemy_startx, enemy_starty, enemy_width, enemy_height, black)
        enemy_startx -= enemy_speed
        enemies_dodged(score)

        
        
            
        if enemy_startx <0:
            enemy_starty = height- 130
            enemy_startx = width - 53
            score += 1
            enemy_speed +=0.2
         
        if x+5 > enemy_startx and x+5 < enemy_startx + enemy_width :
            if y ==  height-200 :
                crash()
        
        pygame.display.update()
        clock.tick(60)

gameloop()
pygame.quit()
sys.exit()
        
