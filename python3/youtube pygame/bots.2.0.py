import pygame
from text_object import *
import random
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 680


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

startX = 5
startY = 5
widht = 16
height = 16
border = 2
speed = 1
ID = 0

EMPTY = (192, 192, 192)
WAll = (128, 128, 128)
BOT = (0, 0, 128)
FOOD = (50, 205, 50)
POISON = (139, 0, 0)
CORPSE = (224, 255, 255)

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
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


class World():
    def __init__(self):
        pygame.init()   
        random.seed()
        self.
        

def getArray(n):
    array = []
    for i in range(8):
        array.append([])
        for y in range(8):
            array[i].append(n)
    return array

class Object():
    def __init__(self,x,y,Type,color):
        self.x = x
        self.y = y
        self.Type = Type
        self.color = color
    
    def getRealX(self):
        return startX + (widht + border) * self.x
    
    def getRealY(self):
        return startY + (height + border) * self.y
    
    def draw(self):
        pygame.draw.rect(window,self.color,(self.getRealX(),self.getRealY(),widht,height))
    
    def move(self,x,y):
        if self.x + x > 0 and self.x + x < len(Map[0]) -1 and self.y + y > 0 and self.y + y < len(Map) - 1:
            self.x += x
            self.y += y
        else:
            print("Go out borders ",self.x + x,self.y + y)



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


class Bot(Object):
    def __init__(self, x, y, health, direction, Type,color):
        super().__init__(x,y,Type,color)
        global Map
        self.alive = True
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

    def moveFromDirection(self,direction):
        x = 0
        y = 0
        direction += self.direction
        if direction >= 8:
            direction -= 8
        if direction in up:
            y -= 1
        if direction in down:
            y += 1
        if direction in left:
            x -= 1
        if direction in right:
            x += 1
        self.move(x,y)

    def do(self):
        global xTarget, yTarget
        sell = self.DNK[self.index]
        if sell <= 7:
            if sell == 0:
                xTarget -= 1
                yTarget -= 1
            if sell == 2:
                xTarget -= 1

    

    def take(self, n):
        pass

    def look(self, n):
        pass
    def turnAround(self, n):
        pass
    



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





def drawWindow():
    
    

    global Map

    window.fill((240, 240, 250))

    for line in range(len(Map)):
        for sell in range(len(Map[line])):
            pygame.draw.rect(window,(getColor(Map[line][sell])),(startX + (widht + border) * sell,startY + (height + border) * line,widht,height))

    #pygame.draw.rect(window, (0, 0, 255), (x, y, widht, height))
    pygame.display.update()




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
   pass

def textInput(x,y,text,color):
    global window
    global fontObj
    textSurfaceObj = fontObj.render(text, True, color)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (x, y)

    #screen.fill(white)
    window.blit(textSurfaceObj, textRectObj)
    

#createPopulation(64,20)
#generation(3,100)
#generation(4,20)

#n = 27
#k = 0
drawWindow()
pygame.image.save(window,"bg.jpg")
bg = pygame.image.load("bg.jpg")
window.blit(bg,(0,0))
a = Object(10,10,"FOOD",FOOD)
b = Bot(20,10,10,6,"BOT",BOT)
while run:
    clock.tick(100)
    window.blit(bg,(0,0))
    a.draw()
    b.draw()
    pygame.display.flip()
    handle_events()
    #update()
    a.move(0,1)
    b.moveFromDirection(2)
    
pygame.quit()
