import pygame
from text_object import *
import random
import copy
import _pickle as cPickle
LOAD_FILE_NAME = "data.txt"
SAVE_FILE_NAME = "data.txt"
LOAD = True
SAVE = True
BOTS_N = 64 # Не изменять!
WALLS_N = 10
POISON_N = 50
FOOD_N = 100

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
BOT_START_HEALTH = 30


class World():
    def __init__(self):
        pygame.init()
        random.seed()
        self.FPS = 30
        self.generation = 1
        self.WINDOW_WIDTH = 1500
        self.WINDOW_HEIGHT = 700
        self.mapL = 80
        self.mapW = 35
        self.clock = pygame.time.Clock()
        self.run = True
        self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.fontObj = pygame.font.Font("font.ttf", 12)
        self.map = self.generationMap()
        pygame.display.set_caption("Bots's world'!")
        self.drawWindow()
        pygame.image.save(self.window,"bg.jpg")

        self.bg = pygame.image.load("bg.jpg")
        self.window.blit(self.bg,(0,0))
        self.objects = Objects()
        #self.data = 

    def generationMap(self):
        Map = []
        for j in range(self.mapW):
            Map.append([])
            for i in range(self.mapL):
                if i == 0 or j == 0 or j == self.mapW - 1 or i == self.mapL - 1:  
                    Map[j].append(1)
                else:
                    Map[j].append(0)
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
        self.handle_events()

    def handle_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.FPS -= 10
        if keys[pygame.K_RIGHT]:
            self.FPS += 10

    # if keys[pygame.K_UP]:
    #    population[ID].yTarget -= speed
    # if keys[pygame.K_DOWN]:
    #    population[ID].yTarget += speed



    def drawObjects(self):
        for i in self.objects.poison:
            i.draw()
        for i in self.objects.walls:
            i.draw()
        for i in self.objects.bots:
            i.draw()
        for i in self.objects.food:
            i.draw()

    def drawText(self):
        self.textInput(30,(startY + (height + border) * self.mapW) + 10,"Max age:",(70, 130, 180))
        self.textInput(100,(startY + (height + border) * self.mapW) + 10,str(self.objects.MaxAge),(70, 130, 180))
        self.textInput(38,(startY + (height + border) * self.mapW) + 30,"Max health:",(70, 130, 180))
        self.textInput(100,(startY + (height + border) * self.mapW) + 30,str(self.objects.MaxHealth),(70, 130, 180))
        self.textInput(15,(startY + (height + border) * self.mapW) + 50,"FPS:",(70, 130, 180))
        self.textInput(100,(startY + (height + border) * self.mapW) + 50,str(self.FPS),(70, 130, 180))
        #self.textInput(200,(startY + (height + border) * self.mapW) + 30,"Medium Health:",(70, 130, 180))
        #self.textInput(250,(startY + (height + border) * self.mapW) + 30,str(self.objects.MediumHealth),(70, 130, 180))
        #self.textInput(200,(startY + (height + border) * self.mapW) + 50,"Medium Age:",(70, 130, 180))
        #self.textInput(250,(startY + (height + border) * self.mapW) + 50,str(self.objects.MediumAge),(70, 130, 180))

    def draw(self):
        self.window.blit(self.bg,(0,0))
        self.drawObjects()
        self.drawText()
        #print("draw",self.objects.ID)
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
        self.MaxPoison = 0
        self.MaxFood = 0
        self.MaxAge = 0
        self.MaxHealth = 0
        self.MediumHealth = 0
        self.MediumAge = 0
    
    def checkCell(self,x,y):
        ret = "EMPTY"
        for cell in self.poison:
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
        self.MaxFood = food
        self.MaxPoison = poison
        if LOAD:
            file = open(LOAD_FILE_NAME,mode="rb")
            a = file.read()

            self.bots = cPickle.loads(a)
            file.close()
        else:
            self.generationBots(bots)

        self.generationPioson(self.MaxPoison)
        self.generationWalls(walls)
        
        self.generationFood(self.MaxFood)

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
            #print("FOOD ",i)
            x, y = self.generationXY()
            self.food.append(Object(x,y,"FOOD",FOOD))

    def copyBot(self,n):
        x , y = self.generationXY()
        bot = copy.deepcopy(self.bots[n])
        bot.alive = True
        bot.Isee = "NONE"
        bot.x = x
        bot.y = y
        bot.health = BOT_START_HEALTH
        bot.step = 0
        bot.index = 0
        bot.age = 0
        return bot 
        random.randint
    def generationNewBots(self):
        self.ID = 0
        world.generation += 1
        for i in range(7):
            for j in range(8):
                self.bots.append(self.copyBot(j))
            
        for j in range(-8,-1,1):
            y = random.randint(0,len(self.bots[0].DNK)-1)
            self.bots[j].DNK[y] = random.randint(0,63)
    

    def updateBots(self):
        print(self.ID)
        if len(self.food) < self.MaxFood // 2:
            self.generationFood(self.MaxFood - len(self.food))
        if len(self.poison) < self.MaxPoison // 2:
            self.generationPioson(self.MaxPoison - len(self.poison))
        if len(self.bots) > 8:
            print(len(self.bots))
            health = 0
            age = 0
            while self.ID < len(self.bots):
                if (self.bots[self.ID].alive == False or self.bots[self.ID].health <= 0) and len(self.bots) > 8:
                    del(self.bots[self.ID]) 
                else:
                    print("BOT DOING")
                    if self.ID < len(self.bots):
                        health += self.bots[self.ID].health
                        age += self.bots[self.ID].age
                        if self.bots[self.ID].age > self.MaxAge:
                            self.MaxAge = self.bots[self.ID].age
                        if self.bots[self.ID].health > self.MaxHealth:
                            self.MaxHealth = self.bots[self.ID].health
                        self.bots[self.ID].do()


                    else:
                        
                        break
            self.MediumAge = age // len(self.bots)
            self.MediumHealth = health // len(self.bots)
            
            self.ID = 0            
            world.draw()
                
        else:
            self.generationNewBots()
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
        self.age = 0
        self.alive = True
        self.act = 0
        self.Isee = "NONE"
        self.direction = direction
        self.index = 0
        self.step = 0
        self.health = health
        self.DNK = self.generetionDNK()

    def generetionDNK(self):
        mass = []
        for i in range(64):
            mass.append(random.randint(0,63))
        return mass

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
        self.index += 1
        x, y  = self.getXY(direction)
        self.health -= 1
        world.objects.ID += 1
        self.age += 1
        if self.x + x > 0 and self.x + x < len(world.map[0]) -1 and self.y + y > 0 and self.y + y < len(world.map) - 1:
            if  world.objects.checkCell(self.x + x,self.y + y) == "EMPTY":
                self.x += x
                self.y += y
                self.Isee = "EMPTY"
            elif  world.objects.checkCell(self.x + x,self.y + y) == "POISON":
                self.x += x
                self.y += y
                self.alive = False
                self.Isee = "POISON"
            elif  world.objects.checkCell(self.x + x,self.y + y) == "WALL":
                self.Isee = "WALL"
            elif  world.objects.checkCell(self.x + x,self.y + y) == "BOT":
                self.Isee = "BOT"
            elif  world.objects.checkCell(self.x + x,self.y + y) == "FOOD":
                self.health += 40
                self.x += x
                self.y += y
                self.Isee = "FOOD" 
                world.objects.deleteObject(self.x,self.y,"FOOD")
        else:
            self.Isee = "WALL"

    def take(self, direction):
        self.index += 1
        direction -= 8
        x, y  = self.getXY(direction)
        self.health -= 1
        world.objects.ID += 1
        self.age += 1
        if self.x + x > 0 and self.x + x < len(world.map[0]) -1 and self.y + y > 0 and self.y + y < len(world.map) - 1:
            if  world.objects.checkCell(self.x + x,self.y + y) == "EMPTY":
                self.Isee = "EMPTY"
            elif  world.objects.checkCell(self.x + x,self.y + y) == "POISON":
                world.objects.deleteObject(self.x + x,self.y + y,"POISON")
                world.objects.food.append(Object(self.x + x,self.y + y,"FOOD",FOOD))
                self.Isee = "POISON"     
            elif  world.objects.checkCell(self.x + x,self.y + y) == "WALL":
                self.Isee = "WALL"
            elif  world.objects.checkCell(self.x + x,self.y + y) == "BOT":
                self.Isee = "BOT"  
            elif  world.objects.checkCell(self.x + x,self.y + y) == "FOOD":
                self.health += 40
                self.Isee = "FOOD" 
                world.objects.deleteObject(self.x + x,self.y + y,"FOOD")
        else:
            self.Isee = "WALL"

    def look(self, direction):
        self.index += 1
        direction -= 8 * 2
        x, y  = self.getXY(direction)
        if self.step <= 10:
            self.step += 1
            if self.x + x > 0 and self.x + x < len(world.map[0]) -1 and self.y + y > 0 and self.y + y < len(world.map) - 1:
                if  world.objects.checkCell(self.x + x,self.y + y) == "EMPTY":
                    self.Isee = "EMPTY"
                elif  world.objects.checkCell(self.x + x,self.y + y) == "POISON":
                    self.Isee = "POISON"
                elif  world.objects.checkCell(self.x + x,self.y + y) == "WALL":
                    self.Isee = "WALL"
                elif  world.objects.checkCell(self.x + x,self.y + y) == "BOT":
                    self.Isee = "BOT"
                elif  world.objects.checkCell(self.x + x,self.y + y) == "FOOD":
                    self.Isee = "FOOD"
            else:
                self.Isee = "WALL"
        else:
            self.step = 0
            world.objects.ID += 1
            self.health -= 1
            self.age += 1

    def turnAround(self, direction):
        self.index += 1
        direction -= 8 * 3
        direction += self.direction
        if direction >= 8:
            direction -= 8

        if self.step <= 10:
            self.step += 1
            if direction == 1:
                self.direction += 2
            if direction == 3:
                self.direction += 4
            if direction == 5:
                self.direction += 6
            if self.direction >= 8:
                self.direction -= 8          
        else:
            self.step = 0
            world.objects.ID += 1
            #self.health -= 1
            self.age += 1

    def getIndexFromIsee(self):
        if self.Isee == "NONE":
            return 0
        if self.Isee == "EMPTY":
            return 5
        if self.Isee == "POISON":
            return 1
        if self.Isee == "WALL":
            return 2
        if self.Isee == "BOT":
            return 3
        if self.Isee == "FOOD":
            return 4

        #if self.Isee = "CORPSE":
         #   self.index = 
        

    def do(self):
        move = range(0,8) #[0,1,2,3,4,5,6,7]
        take = range(8,16) #[8,9,10,11,12,13,14,15]
        look = range(16,24)#[16,17,18,19,20,21,22,23]
        turn = [25,27,29,31]
        jump = range(32,64)
        self.index += self.getIndexFromIsee()
        print("Boot Doing")
        for i in range(10):
            #print("BOOT DOING")
            while self.index >=64:
                self.index -= 64
            print("LEN DNK ",len(self.DNK))
            do = self.DNK[self.index]
    
            if do in move:
                print("Move ",do)
                self.move(do)
                break
            elif do in take:
                print("Take ",do)
                self.take(do)
                break
            elif do in look:
                print("Look ",do)
                self.look(do)
                break
            elif do in turn:
                print("turn ",do)
                self.turnAround(do)
                break
            elif do in jump:
                print("jump ",do)
                self.index += do
                self.age += 1
                world.objects.ID += 1
                self.health -= 1
            else:
                self.health -= 1
                self.step = 0
                self.index += 1
                self.age += 1
                world.objects.ID += 1

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











def update():
   pass


    #screen.fill(white)
    #window.blit(textSurfaceObj, textRectObj)
    

#createPopulation(64,20)
#generation(3,100)
#generation(4,20)


world = World()

world.objects.generationAll(POISON_N,WALLS_N,BOTS_N,FOOD_N) #poison,walls,bots,food
a = Object(10,10,"FOOD",FOOD)
b = Bot(20,10,10,6,"BOT",BOT)
world.update() 

while world.run:
    world.update()  
    world.draw()  
    world.objects.updateBots()
    #world.textInput(500,500,"Hello world" , (200,200,200))

pygame.quit()
if SAVE:
    data = open(SAVE_FILE_NAME,mode ='wb')
    pickled = cPickle.dumps(world.objects.bots)
    #cPickle.dump(world.objects.bots,world.data)
    data.write(pickled)

    data.close()
    print("Data saved")
else:
    print("Data didn't save")
