import pygame
from text_object import *
import random

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
BOT_START_HEALTH = 20


class World():
    def __init__(self):
        pygame.init()
        random.seed()
        self.FPS = 1
        self.WINDOW_WIDTH = 1500
        self.WINDOW_HEIGHT = 700
        self.mapL = 80
        self.mapW = 35
        self.clock = pygame.time.Clock()
        self.run = True
        self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.fontObj = pygame.font.Font(None, 20)
        self.map = self.generationMap()
        pygame.display.set_caption("Bots's world'!")
        self.drawWindow()
        pygame.image.save(self.window,"bg.jpg")

        self.bg = pygame.image.load("bg.jpg")
        self.window.blit(self.bg,(0,0))
        self.objects = Objects()


    def generationMap(self):
        Map = []
        for j in range(self.mapW):
            Map.append([])
            for i in range(self.mapL):
                #print(i)
                if i == 0 or j == 0 or j == self.mapW - 1 or i == self.mapL - 1:  
                    Map[j].append(1)
                else:
                    Map[j].append(0)
        #print(Map)
        return Map

    def drawWindow(self):

        self.window.fill((240, 240, 250))

        for line in range(len(self.map)):
            for sell in range(len(self.map[line])):
                pygame.draw.rect(self.window,(getColor(self.map[line][sell])),(startX + (widht + border) * sell,startY + (height + border) * line,widht,height))

        #pygame.draw.rect(window, (0, 0, 255), (x, y, widht, height))
        pygame.display.flip()

    def update(self):
        self.clock.tick(self.FPS)
        handle_events()

    def drawObjects(self):
        for i in self.objects.poison:
            i.draw()
        for i in self.objects.walls:
            i.draw()
        for i in self.objects.bots:
            i.draw()
        for i in self.objects.food:
            i.draw()

    def draw(self):
        self.window.blit(self.bg,(0,0))
        self.drawObjects()
        pygame.display.flip()

    def textInput(self,x,y,text,color):
        textSurfaceObj = self.fontObj.render(text, True, color)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (x, y)
        self.window.blit(textSurfaceObj, textRectObj)


def getArray(n):
    array = []
    for i in range(8):
        array.append([])
        for y in range(8):
            array[i].append(n)
    return array

class Objects():
    """docstring for Obj"""
    def __init__(self):
        self.ID = 0
        self.poison = []
        self.walls = []
        self.bots = []
        self.food = []
    
    def checkCell(self,x,y):
        ret = "EMPTY"
        print("#######",len(self.poison)) 
        for cell in self.poison:
            #print("POis", cell.x ,cell.y)
            if x == cell.x and y == cell.y:
                ret = cell.Type
        for cell in self.walls:
            if x == cell.x and y == cell.y:
                ret = cell.Type
        for cell in self.bots:
            if x == cell.x and y == cell.y:
                ret = cell.Type
        for cell in self.food:
            if x == cell.x and y == cell.y:
                ret = cell.Type
        return ret

    def deleteObject(self,x,y,Type):
        i = self.findObject(x,y,Type)
        print("Bots x y i",x,y,i)
        if Type == "FOOD":
            self.food.pop(i)
        if Type == "POISON":
            self.poison.pop(i)
        
    def findObject(self,x,y,Type):
        if Type == "FOOD":
            i = 0
            while i < len(self.food):
                if self.food[i].x == x and self.food[i].y == y:
                    return i
                i += 1 
        elif Type == "POISON":
            i = 0
            while i < len(self.poison):
                print("POISON X Y ", self.poison[i].x,self.poison[i].y)
                if self.poison[i].x == x and self.poison[i].y == y:
                    return i
                i += 1 

    def generationXY(self):
        x = 1
        y = 1
        while self.checkCell(x,y) != "EMPTY":
            x = random.randint(1,len(world.map[0]) -2)
            y = random.randint(1,len(world.map) - 2)
        return x,y

    def generationAll(self,poison,walls,bots,food):
        self.generationPioson(poison)
        self.generationWalls(walls)
        self.generationBots(bots)
        self.generationFood(food)

    def generationPioson(self,n):
        for i in range(n):
            x, y = self.generationXY()
            self.poison.append(Object(x,y,"POISON",POISON))

    def generationWalls(self,n):
        for i in range(n):
            x, y = self.generationXY()
            self.walls.append(Object(x,y,"WALL",WAll))

    def generationBots(self,n):
        def generationDirection():
            mass = [0,2,4,6]
            return mass[random.randint(0,3)]

        for i in range(n):
            x, y = self.generationXY()
            self.bots.append(Bot(x,y,BOT_START_HEALTH,generationDirection(),"BOT",BOT))

    def generationFood(self,n):
        for i in range(n):
            x, y = self.generationXY()
            self.food.append(Object(x,y,"FOOD",FOOD))

    def updateBots(self):
        while self.ID < len(self.bots):
            if self.bots[self.ID].alive == False or self.bots[self.ID].health <= 0:
                del(self.bots[self.ID]) 
            if self.ID < len(self.bots):
                a = random.randint(0,8)
                #print(a,self.bots[self.ID].direction)
                self.bots[self.ID].take(a)
                #self.bots[self.ID].draw()
            else:
                break
        world.draw()
        self.ID = 0



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
        pygame.draw.rect(world.window,self.color,(self.getRealX(),self.getRealY(),widht,height))
    
    def move(self,x,y):
        if self.x + x > 0 and self.x + x < len(world.map[0]) -1 and self.y + y > 0 and self.y + y < len(world.map) - 1:
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
        self.alive = True
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

    def getXY(self,direction):
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
        return x,y

    def move(self,direction):
        x, y  = self.getXY(direction)
        self.health -= 1
        if self.x + x > 0 and self.x + x < len(world.map[0]) -1 and self.y + y > 0 and self.y + y < len(world.map) - 1:
            if  world.objects.checkCell(self.x + x,self.y + y) == "EMPTY":
                self.x += x
                self.y += y
                self.Isee = "EMPTY"
                world.objects.ID += 1
            elif  world.objects.checkCell(self.x + x,self.y + y) == "POISON":
                self.x += x
                self.y += y
                self.alive = False
                self.Isee = "POISON"
                world.objects.ID += 1
            elif  world.objects.checkCell(self.x + x,self.y + y) == "WALL":
                self.Isee = "WALL"
                world.objects.ID += 1
            elif  world.objects.checkCell(self.x + x,self.y + y) == "BOT":
                self.Isee = "BOT"
                world.objects.ID += 1
            elif  world.objects.checkCell(self.x + x,self.y + y) == "FOOD":
                self.health += 20
                self.x += x
                self.y += y
                self.Isee = "FOOD" 
                world.objects.deleteObject(self.x,self.y,"FOOD")
                world.objects.ID += 1
        else:
            self.Isee = "WAll"
            world.objects.ID += 1

    def take(self, direction):
        direction -= 8
        x, y  = self.getXY(direction)
        self.health -= 1
        if self.x + x > 0 and self.x + x < len(world.map[0]) -1 and self.y + y > 0 and self.y + y < len(world.map) - 1:
            if  world.objects.checkCell(self.x + x,self.y + y) == "EMPTY":
                self.Isee = "EMPTY"
                world.objects.ID += 1
            elif  world.objects.checkCell(self.x + x,self.y + y) == "POISON":
                world.objects.deleteObject(self.x + x,self.y + y,"POISON")
                world.objects.food.append(Object(self.x + x,self.y + y,"FOOD",FOOD))
                self.Isee = "POISON"
                world.objects.ID += 1
            elif  world.objects.checkCell(self.x + x,self.y + y) == "WALL":
                self.Isee = "WALL"
                world.objects.ID += 1
            elif  world.objects.checkCell(self.x + x,self.y + y) == "BOT":
                self.Isee = "BOT"
                world.objects.ID += 1
            elif  world.objects.checkCell(self.x + x,self.y + y) == "FOOD":
                self.health += 20
                self.Isee = "FOOD" 
                world.objects.deleteObject(self.x + x,self.y + y,"FOOD")
                world.objects.ID += 1
        else:
            self.Isee = "WAll"
            world.objects.ID += 1

    def look(self, n):
        pass
    def turnAround(self, n):
        pass


    def do(self):
        global xTarget, yTarget
        sell = self.DNK[self.index]
        if sell <= 7:
            if sell == 0:
                xTarget -= 1
                yTarget -= 1
            if sell == 2:
                xTarget -= 1

    def draw(self):
        pygame.draw.rect(world.window,self.color,(self.getRealX(),self.getRealY(),widht,height))
        world.textInput(self.getRealX() + widht / 2, self.getRealY() + widht / 2,str(self.health),(255,255,255))

    
    



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









def handle_events():

    global population, run

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            world.run = False

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


    #screen.fill(white)
    #window.blit(textSurfaceObj, textRectObj)
    

#createPopulation(64,20)
#generation(3,100)
#generation(4,20)
world = World()

world.objects.generationAll(100,10,50,10) #poison,walls,bots,food
a = Object(10,10,"FOOD",FOOD)
b = Bot(20,10,10,6,"BOT",BOT)
world.update() 

while world.run:
    world.update()    
    world.objects.updateBots()
    #world.textInput(500,500,"Hello world" , (200,200,200))
pygame.quit()

