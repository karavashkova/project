from random import randint
import pygame
from pygame.locals import *
from pygame.constants import *
from pygame.draw import *
from time import time
import sys


pygame.init()





screen = pygame.display.set_mode((890, 890), pygame.DOUBLEBUF, 32)
backscreen = pygame.image.load('/home/qrewetka/Документы/cat/backscreen.jpeg')
backscreen1 = pygame.image.load('/home/qrewetka/Документы/cat/backscreen1.png')
backscreen2 = pygame.image.load('/home/qrewetka/Документы/cat/backscreen2.jpeg')
backscreen3 = pygame.image.load('/home/qrewetka/Документы/cat/backscreen3.jpeg')
catscreen = pygame.image.load('/home/qrewetka/Документы/cat/cat.png')

lifescreen = pygame.image.load('/home/qrewetka/Документы/cat/life.png')
sum = 0






menu = []
foodscreen = []

x = 400

xf = 445
yf = 900
vf = randint(5, 10)

def setnewfood():
    
    global xf, vf, yf, s, menu, foodscreen

    menu = ['/home/qrewetka/Документы/cat/food.png', '/home/qrewetka/Документы/cat/food2.png', '/home/qrewetka/Документы/cat/food3.png', '/home/qrewetka/Документы/cat/food4.png', '/home/qrewetka/Документы/cat/food5.png', '/home/qrewetka/Документы/cat/food6.png']
    foodscreen = pygame.image.load(menu[s])
    xf = randint(90, 800)
    yf = -10

    vf = randint(1, 3)
    
def setlife():
    global i
    screen.blit(lifescreen, (20+65*i, 20))

life = 3

seconds = 2000

s = 0
yf = 900
v = 0


setnewfood()
while 1 == 1:
    click1 = False
    while click1 == False:
        screen.blit(backscreen1, (0, 0))
        for i in pygame.event.get():
            if i.type == pygame.KEYDOWN :
                if i.key == pygame.K_SPACE:
                    click1 = True
            if i.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()

    finished = True

    while finished == True:

        fontObj = pygame.font.Font('freesansbold.ttf', 30)
        textSurfaceObj = fontObj.render(str(sum), True, (0, 0, 0))
        seconds+=1


        x = x+v
        yf = yf+vf

        screen.blit(backscreen, (0, 0))
        screen.blit(catscreen, (x, 740))
        screen.blit(foodscreen, (xf, yf))
        screen.blit(textSurfaceObj, (800, 40))
        
        if life>0:
            for i in range(life):
                setlife()
        else:
            finished = False
            

        if yf > 890 and s==3:
            
            s = randint(0, len(menu)-1)
            setnewfood()
        elif yf > 890:
            life-=1
            s = randint(0, len(menu)-1)
            setnewfood()




        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()
            elif i.type == pygame.KEYDOWN :
                if i.key == pygame.K_LEFT:
                    if seconds<=2000:
                        v = -6
                    else:
                        v = -3
                elif i.key == pygame.K_RIGHT:
                    if seconds<=2000:
                        v = 6
                    else:
                        v = 3
                elif i.key == pygame.K_ESCAPE:
                    finished = False
            elif i.type == pygame.KEYUP:
                if (i.key == pygame.K_LEFT) or (i.key == pygame.K_RIGHT):
                    v = 0
                
        if ((xf> x+70) and (xf<x+120)) and ((yf>760)):
            if s==3:
                life-=1
                s = randint(0, len(menu)-1)

            elif life<3 and s==4:
                life+=1
                s = randint(0, len(menu)-1)

            elif s==5:
                seconds=0
                s = randint(0, len(menu)-1)

            else:
                sum+=10*(s+1)
                s = randint(0, len(menu)-1)
            
            setnewfood()

        pygame.display.update()

    click2 = False

    while click2 == False:
        if life == 0:
            screen.blit(backscreen2, (0, 0))
        elif life > 0:
            screen.blit(backscreen3, (0, 0))
        pygame.display.update()
        for i in pygame.event.get():
            if i.type == pygame.KEYDOWN :
                if i.key == pygame.K_SPACE:
                    click2 = True
                    finished = True
            if i.type == pygame.QUIT:
                sys.exit()





