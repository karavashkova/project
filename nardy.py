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





X = [1132, 1046, 960, 1132, 1046, 960, 1132, 1046, 960, 1132, 1046, 960]  # координаты фишек
Y = [85, 85, 85, 170, 170, 170, 255, 255, 255, 340, 340, 340] #координаты фишек
Xc = [1132, 1046, 960, 874, 788, 700, 516, 429, 342, 255, 168, 81] 

a = [] #для курсора
C = [0, 0]

bones = ['/home/qrewetka/Изображения/0.png', '/home/qrewetka/Изображения/1.png','/home/qrewetka/Изображения/2.png', '/home/qrewetka/Изображения/3.png', '/home/qrewetka/Изображения/4.png','/home/qrewetka/Изображения/5.png','/home/qrewetka/Изображения/6.png']


l = len(X)

clickt = True
finished = True

s = 0
h = True



def click (event):
    
    global a, h, clickt
    
    a=(event.pos[0], event.pos[1])
    h = not h
    clickt = not clickt


class chip(object):
    def __init__(self, index):
        self.index = index
    
    def x1(self):
        return X[self.index]

    def y1(self):
        return Y[self.index]
    
    def set(self):
        screen.blit(chipscreen, (self.x1()-37, self.y1()-37))


chiplist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


for i in range (l):
    chiplist[i-1] = chip(i)


while finished == True:

    screen.blit(backscreen, (0, 0, 0, 0))
    for i in range (l):
        chip.set(chiplist[i-1])
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = False
        elif event.type == MOUSEBUTTONDOWN:
            click(event)
            
            
            for i in range (l):                
                if ((a[0]-X[i-1])**2 + (a[1]-Y[i-1])**2)**0.5 <= 25 and (clickt == False):
                    s=i-1
                    X[s] = a[0]
                    Y[s] = a[1]
                    
                                            
        elif pygame.mouse.get_focused() and (h == False):
            
            a = pygame.mouse.get_pos()
            X[s] = a[0]-37
            Y[s] = a[1]-37

        
    

    
    pygame.display.update()



    
    
                
    
                   


    