import pygame
from text_object import *
import random
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800


pygame.init()
random.seed()
clock = pygame.time.Clock()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
fontObj = pygame.font.Font(None, 20)
pygame.display.set_caption("Bots's world'!")

#x = 2
#y = 2
#xTarget = x
#yTarget = y

up = [0, 1, 2]
down = [6, 5, 4]
left = [0, 7, 6]
right = [2, 3, 4]


widht = 16
height = 16
border = 2
speed = 1
ID = 0

run = True

Map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


def getArray(n):
    array = []
    for i in range(8):
        array.append([])
        for y in range(8):
            array[i].append(n)
    return array


class Bot():
    def __init__(self, x, y, health, direction):
        global Map
        self.alive = True
        self.x = x
        self.y = y
        #print(self.x,self.y)
        Map[y][x] = 2
        self.xTarget = x
        self.yTarget = y
        self.act = 0
        self.Isee = 0
        self.direction = direction
        self.index = 0
        self.step = 0
        self.health = height
        self.DNK = [0, 1, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0]

    def do(self):
        global xTarget, yTarget
        sell = self.DNK[self.index]
        if sell <= 7:
            if sell == 0:
                xTarget -= 1
                yTarget -= 1
            if sell == 2:
                xTarget -= 1

    def move(self, n):
        self.health -= 1
        self.act = 'move'
        command = n + self.direction
        if command > 7:
            command -= 8
        if command in up:
            self.yTarget -= 1
        if command in down:
            self.yTarget += 1
        if command in left:
            self.xTarget -= 1
        if command in right:
            self.xTarget += 1

    def take(self, n):
        self.health -= 1
        self.act = 'take'
        command = n + self.direction - 8
        if command > 7:
            command -= 8
        if command in up:
            self.yTarget -= 1
        if command in down:
            self.yTarget += 1
        if command in left:
            self.xTarget -= 1
        if command in right:
            self.xTarget += 1

    def look(self, n):
        self.act = 'look'
        population[ID].step += 1
        command = n + self.direction - 8 * 2
        if command > 7:
            command -= 8
        if command in up:
            self.yTarget -= 1
        if command in down:
            self.yTarget += 1
        if command in left:
            self.xTarget -= 1
        if command in right:
            self.xTarget += 1

    def turnAround(self, n):
        population[ID].step += 1
        if n == 24:
            self.direction += 2
        if n == 25:
            self.direction += 4
        if n == 26:
            self.direction += 6
        if self.direction > 6:
            self.direction -= 8

    def go(self):
        global Map
        Map[self.y][self.x], Map[self.yTarget][self.xTarget] = 0, 2
        self.x = self.xTarget
        self.y = self.yTarget




def getXY():
    x = 1
    y = 1
    while Map[y][x] != 0:
        x = random.randint(1,len(Map[0]) -2)
        y = random.randint(1,len(Map) -2) 
    Map[y][x] = 2
    return x, y

def generation(that,n):
    for i in range(n):
        x = 1
        y = 1
        while Map[y][x] != 0:
            x = random.randint(1,len(Map[0]) -2)
            y = random.randint(1,len(Map) -2) 
        Map[y][x] = that
def createPopulation(n,health):
    direction = 2
    global population 
    population = []
    mass = [0,2,4,6]
    #population.append(Bot(10,10,,2))

    for i in range(n):
        a ,b=getXY() 
        direction =mass[random.randint(0,3)] 
        population.append(Bot(a,b,health,direction))

#population[ID] = 


def getColor(color):
    if color == 0:  # EMPTY
        return (192, 192, 192)
    if color == 1:  # WAll
        return (128, 128, 128)
    if color == 2:  # BOT
        return (0, 0, 128)
    if color == 3:  # FOOD
        return (50, 205, 50)
    if color == 4:  # POISON
        return (139, 0, 0)
    if color == 5:  # CORPSE
        return (224, 255, 255)


def drawWindow():
    global startX , startY
    startX = 5
    startY = 5

    global Map

    window.fill((240, 240, 250))

    for line in range(len(Map)):
        for sell in range(len(Map[line])):
            a = getColor(Map[line][sell])
            pygame.draw.rect(window, a, (startX + (
                widht + border) * sell, startY + (height + border) * line, widht, height))
            
    textInput(startX + (widht + border) * population[ID].x + widht / 2,startY + (height + border) *population[ID].y + height / 2,str(population[ID].health),(255,255,255))
    #pygame.draw.rect(window, (0, 0, 255), (x, y, widht, height))
    pygame.display.flip()

    #pygame.display.update()

def drawCells(color1,color2):
    
    pygame.draw.rect(window, color1, (startX + (widht + border) * population[ID].xTarget, startY + (height + border) * population[ID].yTarget, widht, height))
    pygame.draw.rect(window, color2, (startX + (widht + border) * population[ID].x, startY + (height + border) * population[ID].y, widht, height))
    textInput(startX + (widht + border) * population[ID].x + widht / 2,startY + (height + border) *population[ID].y + height / 2,str(population[ID].health),(255,255,255))
    pygame.display.flip()

def updateCounters():
    global population , ID
    population[ID].xTarget = population[ID].x
    population[ID].yTarget = population[ID].y
    population[ID].step = 0
    ID += 1

def handle_events():

    global population, run

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT]:
    #    population[ID].xTarget -= speed
    # if keys[pygame.K_RIGHT]:
    #    population[ID].xTarget += speed

    # if keys[pygame.K_UP]:
    #    population[ID].yTarget -= speed
    # if keys[pygame.K_DOWN]:
    #    population[ID].yTarget += speed


def update():
    global population , Map, ID
    if population[ID].alive and population[ID].health != 0: 
        if population[ID].step >= 10:
            population[ID].step = 0
            population[ID].health -= 1
            ID += 1 
        elif population[ID].act == 'move':
            if Map[population[ID].yTarget][population[ID].xTarget] == 0:  # EMPTY
                population[ID].Isee = 0
                population[ID].go()
                drawCells((0, 0, 128),(192, 192, 192))
                updateCounters()
            elif Map[population[ID].yTarget][population[ID].xTarget] == 1:  # Wall
                population[ID].Isee = 1
                updateCounters()
            elif Map[population[ID].yTarget][population[ID].xTarget] == 2:  # BOT
                population[ID].Isee = 2
                updateCounters()
            elif Map[population[ID].yTarget][population[ID].xTarget] == 3:  # FOOD
                population[ID].Isee = 3
                population[ID].health += 20
                population[ID].go()
                drawCells((0, 0, 128),(192, 192, 192))
                updateCounters()
            elif Map[population[ID].yTarget][population[ID].xTarget] == 4:  # POISON
                population[ID].Isee = 4
                population[ID].alive = False
                population[ID].go()
                drawCells((0, 0, 128),(192, 192, 192))
                updateCounters()
            elif Map[population[ID].yTarget][population[ID].xTarget] == 5:  # CORPSE
                population[ID].Isee = 5
                updateCounters()

        elif population[ID].act == 'take':
            if Map[population[ID].yTarget][population[ID].xTarget] == 0:  # EMPTY
                population[ID].Isee = 0
                updateCounters()
            elif Map[population[ID].yTarget][population[ID].xTarget] == 1:  # Wall
                population[ID].Isee = 1
                updateCounters()
            elif Map[population[ID].yTarget][population[ID].xTarget] == 2:  # BOT
                population[ID].Isee = 2
                updateCounters()
            elif Map[population[ID].yTarget][population[ID].xTarget] == 3:  # FOOD
                population[ID].Isee = 3
                population[ID].health += 20
                Map[population[ID].yTarget][population[ID].xTarget] = 0
                drawCells((192, 192, 192),(0, 0, 128))
                updateCounters()
            elif Map[population[ID].yTarget][population[ID].xTarget] == 4:  # POISON
                population[ID].Isee = 4
                population[ID].step = 0
                drawCells((50, 205, 50),(0, 0, 128))
                updateCounters()
            elif Map[population[ID].yTarget][population[ID].xTarget] == 5:  # CORPSE
                population[ID].Isee = 5
                updateCounters()
        elif population[ID].act == 'look':
            if Map[population[ID].yTarget][population[ID].xTarget] == 0:  # EMPTY
                population[ID].Isee = 0
                updateCounters()
            elif Map[population[ID].yTarget][population[ID].xTarget] == 1:  # Wall
                population[ID].Isee = 1
                updateCounters()
            elif Map[population[ID].yTarget][population[ID].xTarget] == 2:  # BOT
                population[ID].Isee = 2
                updateCounters()
            elif Map[population[ID].yTarget][population[ID].xTarget] == 3:  # FOOD
                population[ID].Isee = 3
                updateCounters()
            elif Map[population[ID].yTarget][population[ID].xTarget] == 4:  # POISON
                population[ID].Isee = 4
                updateCounters()
            elif Map[population[ID].yTarget][population[ID].xTarget] == 5:  # CORPSE
                population[ID].Isee = 5
                updateCounters()

    else:
        del(population[ID])

    if ID >= len(population):
        ID = 0


def textInput(x,y,text,color):
    global window
    global fontObj
    textSurfaceObj = fontObj.render(text, True, color)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (x, y)

    #screen.fill(white)
    window.blit(textSurfaceObj, textRectObj)
    

createPopulation(64,20)
generation(3,100)
generation(4,20)

n = 0
k = 24
drawWindow()
pygame.time.delay(1000)
while run:
    #textF()
    while ID <= len(population):
        clock.tick(50)
        if n < 8:
            population[ID].move(n)
        elif n > 8 and n < 16:
            population[ID].take(n + 8)
        #elif n > 16 and n < 24:
            #population[ID].look(n + 8*2)
        #elif n > 24:
            #population[ID].turnAround(k)
        
        print(ID,population[ID].yTarget,population[ID].xTarget,ID,len(population))
        handle_events()
        update()
        #textF()
        if len(population) == 0:
            break
        
        n += 1
        if n == 28:
            n = 0
        k +=1
        
        
        #print(getXY())
        #print(ID,population[ID].xTarget,population[ID].yTarget,population[ID].step)
    drawWindow()
pygame.quit()
