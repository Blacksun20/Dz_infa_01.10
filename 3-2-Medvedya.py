import pygame
import math
from pygame.draw import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((800, 1000))

CYAN = (0, 255, 255)
SNOW_WHITE = (230, 230, 230)
BLACK = (0, 0, 0)
LIGHT_BLUE = (161, 249, 228)
DIRTY_LIGHT_BLUE = (220, 247, 218)
MILK = (255, 246, 213)
GREY = (77, 77, 77)
SEA_BLUE = (22, 80, 68)
LIGHT_GREY = (127, 127, 127)
BLUE_GREY = (191, 203, 200)
SKY_BLUE = (121, 121, 242)
DARK_GREY = (126, 132, 140)
RED = (136, 0, 21)

def fon():
    '''
    Программа рисует фон: снег, небо и граница
    '''
    rect(screen, CYAN, (0, 0, 800, 500), 0)
    rect(screen, SNOW_WHITE, (0, 500, 800, 1000), 0)
    line(screen, BLACK, (0, 500), (800, 500))

def nebo(x, y):
    '''
    Программа рисует круги на небе

    '''
    
    r = int(240*k)
    A = 15
    circle(screen, LIGHT_BLUE, (x, y-A), r)
    circle(screen, CYAN, (x, y-A), int((240-50)*k))
    def perecladina1(x, y):
        '''
        
        Программа рисует горизонтальную перекладину

        '''
        polygon(screen, LIGHT_BLUE, [(x-r-5, y-int(25*k)-5-A), (x-r-5, y+int(15*k)-5-A),(x+r+5, y+int(25*k)+5-A), (x+r+5, y-int(15*k)+5-A)], 0)
        polygon(screen, DIRTY_LIGHT_BLUE, [(x-r, y-int(25*k)-5-A), (x-r, y+int(15*k)-5-A), (x-r+int(50*k), y+int(15*k)-5-A), (x-r+int(50*k), y-int(25*k)-3-A)], 0)
        polygon(screen, DIRTY_LIGHT_BLUE, [(x+r, y-int(15*k)+5-A), (x+r, y+int(25*k)+5-A), (x+r-int(50*k), y+int(25*k)+5-A), (x+r-int(50*k), y-int(15*k)+5-A)], 0)
        circle(screen, MILK, (x-r+15, y-10-A), 15)
        circle(screen, MILK, (x+r-17, y+10-A), 15)
   
    def pereckladina2(x, y):
        '''
        Программа рисует вертикальную перекладину

        '''
        polygon(screen, LIGHT_BLUE, [(x-40, y+r+5-A), (x-4, y+r+8-A),(x+40, y-r-10-A), (x-5, y-r-10-A)], 0)
        polygon(screen, DIRTY_LIGHT_BLUE, [(x-40, y+r-3-A), (x-4, y+r+1-A), (x+2, y+r-int(50*k)-A), (x-35, y+r-int(50*k)-5-A)], 0)
        circle(screen, MILK, (x-20, y+r-20-A), 15)
    def krug(x, y):
        '''
        Программа рисует круг по центру

        '''
        circle(screen, MILK, (x, y-A), 25)
    perecladina1(x, y)
    pereckladina2(x, y)
    krug(x, y)

def luja(a, b, c, d):
    '''
    Программа рисует лужу

    '''
    ellipse(screen, GREY, (a, b, c, d), 0)
    ellipse(screen, BLACK, (a, b, c, d), 1)
    ellipse(screen, SEA_BLUE, (a+40, b+int(40*k), c-2*int(40*k), d-int(40*k)), 0)
    ellipse(screen, BLACK, (a+40, b+int(40*k), c-2*int(40*k), d-int(40*k)), 1)

def medved(x, y, n, l, color):
    '''
    Программа рисует медведя

    '''
    def body(x, y, n, l, color):
        '''
        Программа рисует тело 

        '''
        ellipse(screen, color, (x, y, int(260/n), int(450*k/n)), 0)
        ellipse(screen, BLACK, (x, y, int(260/n), int(450*k/n)), 1)

        ellipse(screen, color, (x+int(140/n), y+int(320/n*k), int(190/n), int(150*k/n)), 0)
        ellipse(screen, BLACK, (x+int(140/n), y+int(320/n*k), int(190/n), int(150*k/n)), 1)

        ellipse(screen, color, (x+int(255/n), y+int(440/n*k), int(140/n), int(50*k/n)), 0)
        ellipse(screen, BLACK, (x+int(255/n), y+int(440/n*k), int(140/n), int(50*k/n)), 1)

        ellipse(screen, color, (x+int(210/n), y+int(100/n*k), int(115/n), int(50*k/n)), 0)
        ellipse(screen, BLACK, (x+int(210/n), y+int(100/n*k), int(115/n), int(50*k/n)), 1)
    
        ellipse(screen, color, (x+int(130/n), y-int(70/n*k), int(180/n), int(95*k/n)), 0)
        ellipse(screen, BLACK, (x+int(130/n), y-int(70/n*k), int(180/n), int(95*k/n)), 1)
    def ear(x, y, n, l, color):
        '''
        Рисует уши
        '''
        circle(screen, color, (x+int(155/n) ,y-int(50/n*k)), int(15/n))
        circle(screen, BLACK, (x+int(155/n), y-int(50/n*k)), int(15/n), 1)
    def eye(x, y, n, l, color):
        '''
        рисует глаза

        '''
        circle(screen, color, (x+int(210/n), y-int(35/n*k)), 5)
        circle(screen, BLACK, (x+int(210/n), y-int(35/n*k)), 5)
    def nose(x, y, n, l, color):
        '''
        рисует нос

        '''
        circle(screen, color, (x+int(310/n), y-int(30/n*k)), 5)
        circle(screen, BLACK, (x+int(310/n), y-int(30/n*k)), 5)
    def month(x, y, n, l):
        '''
        рисует рот

        '''
        line(screen, BLACK, (x+int(210/n), y), (x+int(270/n), y))
        line(screen, BLACK, (x+int(270/n), y), (x+int(308/n), y-int(18/n*k)), 1)
    def udochka(x, y, n, l):
        '''
        рисует удочку

        '''
        line(screen, BLACK, (x+int(260/n), y+int((210)/n*k)), (x+int(289/n), y+int((210-55-8)/n*k)), 5)
        line(screen, BLACK, (x+int(318/n), y+int(115/n*k)), (x+int(665/n), y-int(150/n*k)), 5)
        line(screen, BLACK, (x+int(665/n), y-int(150/n*k)), (x+int(665/n)+5, y+int(400/n*k)-2+l), 1)
    body(x, y, n, l, color)
    ear(x, y, n, l, color)
    eye(x, y, n, l, color)
    nose(x, y, n, l, color)
    month(x, y, n, l)
    udochka(x, y, n, l)
    
def vedro(x, y):
    '''
    рисует ведро с рыбкой

    '''
    polygon(screen, LIGHT_GREY, [(x-32,y), (x-20,y+85), (x-20+40,y+85), (x+32,y)], 0)
    polygon(screen, BLACK, [(x-32,y), (x-20,y+85), (x-20+40,y+85), (x+32,y)], 2)
    circle(screen, BLACK, (x,y-32), 46, 2)
    circle(screen, SNOW_WHITE, (x,y-32), 44, 0)
    polygon(screen, SNOW_WHITE, [(x-64,y), (x-64,y-80), (x+64,y-80), (x+64,y)], 0)
    ellipse(screen, BLACK, (x-32, y-47, 65, 94), 2)
    polygon(screen, LIGHT_GREY, [(x-30, y+14), (x-20, y+85), (x+20, y+85), (x+30, y+14)], 0)
    polygon(screen, BLACK, [(x-30, y+14), (x-20, y+85), (x+20, y+85), (x+30, y+14)], 2)
    line(screen, LIGHT_GREY, (x-29, y+14), (x+29, y+14), 2)

    polygon(screen, BLUE_GREY, [(x-21.6, y+8), (x+20, y-30), (x, y+14)], 0)
    polygon(screen, BLACK, [(x-21.6, y+8), (x+20, y-30), (x, y+14)], 2)

    circle(screen, BLACK, (x, y-2), 6)
    circle(screen, SKY_BLUE, (x, y-2), 5)
    circle(screen, DARK_GREY, (x+1, y-2), 2)
    line(screen, BLACK, (x, y+14), (x+20, y-10), 3)



k = 1000/1123

fon()
nebo(480, int(200*k))
luja(800-350, 520+int(160*k), 400,int(180*k))
medved(150, 575-int(136*k), 1.5, 30, SNOW_WHITE)
vedro(600, 900)
vedro(450, 600)
medved(325, 675, 2.5, 0, RED)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
