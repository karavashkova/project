from random import randint
import pygame
from pygame.locals import *
from pygame.constants import MOUSEBUTTONDOWN
from pygame.draw import *
import os


pygame.init()

screen = pygame.display.set_mode((1325, 900), pygame.DOUBLEBUF, 32)

backscreen = pygame.image.load('/home/qrewetka/Изображения/background.png')
chipscreen = pygame.image.load('/home/qrewetka/Изображения/chip.png')
bonescreen = pygame.image.load('/home/qrewetka/Изображения/0.png')
againbuttonscreen = pygame.image.load('/home/qrewetka/Изображения/again.png')


finished = True

def click (event):
    
    global a
    a=(event.pos[0], event.pos[1])

bones = ['/home/qrewetka/Изображения/0.png', '/home/qrewetka/Изображения/1.png','/home/qrewetka/Изображения/2.png', '/home/qrewetka/Изображения/3.png', '/home/qrewetka/Изображения/4.png','/home/qrewetka/Изображения/5.png','/home/qrewetka/Изображения/6.png']

X=[1132, 1048, 960, 877, 792, 515, 430, 345, 260, 175, 90]
Y=[45, 70]

P1=[1092, 1007, 918, 830, 740, 655, 480, 390, 302, 214, 125, 38]
X = [90, 175, 260, 345, 430, 515, 705, 790, 875, 960, 1051, 1136]
b1=0
b2=0
que=3

while finished == True:

    screen.blit(backscreen, (0, 0, 0, 0))
    screen.blit(chipscreen, (P1[0]+4, Y[0]))
    screen.blit(chipscreen, (P1[que]+4, Y[1]))
    bonescreen = pygame.image.load(bones[b1])
    screen.blit(bonescreen, (210, 400))
    bonescreen = pygame.image.load(bones[b2])
    screen.blit(bonescreen, (250, 400))
    screen.blit(againbuttonscreen, (290, 400))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = False
        elif event.type == MOUSEBUTTONDOWN:
            a=[]
            click(event) 

            if (a[0] >= 290 and a[0] <= 320) and (a[1] >= 400 and a[1] <= 430):
                b1=randint(1,6)
                b2=randint(1,6)
            for i in range(0, 12):
                if (a[0] <= P1[i] and a[0] >= P1[i+1]) and (a[1] <= 100):
                    que=que+b1+b2



    
    
                
    
                   


    