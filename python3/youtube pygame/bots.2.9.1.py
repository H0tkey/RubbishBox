import pygame
from text_object import *
import random
import copy
import _pickle as cPickle
import time
#from os import slep

LOAD_FILE_NAME = "testData1.txt"
SAVE_FILE_NAME = "testData1.txt"
LOAD = False
SAVE = True
BOTS_N = 100 
WALLS_N = 159
POISON_N = 250
FOOD_N = 200

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

class Mouse():
    def __init__(self):
        self.x = 0
        self.y = 0

    def update(self):
        if pygame.mouse.get_pressed()[0]:
            self.x , self.y = pygame.mouse.get_pos()
            #print("True")
            return True
        else:
            #print('False')
            return False


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
        self.startTime = time.time()
        self.stopMode = False
        self.workTime = 0
        self.colors = [(173, 255, 47),(0, 255, 127),(0, 255, 255),(70, 130, 180),(178, 34, 34),(255, 255, 0),(148, 0, 211)]
        self.selectedColor = 0
        self.selectedBots = []

    def stop(self):
        mouse = Mouse()
        while self.stopMode:
            self.update()
            if  mouse.update():
                for bot in self.objects.bots:
                    #IF MOUSE ON BOT
                    if bot.getRealX() <= mouse.x and bot.getRealX() + widht >= mouse.x  and bot.getRealY() <= mouse.y and bot.getRealY() + height >= mouse.y: 
                        bot.selected = not(bot.selected)
                        bot.selectedColor = self.colors[self.selectedColor]
                time.sleep(0.1)
            self.draw()
            #time.sleep(100)

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

    def copyBots(self):
        for bot in self.objects.bots:
            if bot.selected:
                if bot.selectedColor == self.colors[self.selectedColor]:
                    self.selectedBots.append(copy.deepcopy(bot))
                    print("Bot coped")

    def insertBots(self):
        self.objects.bots = []
        print(len(self.objects.bots))
        for i in range(BOTS_N):
            bot = copy.deepcopy(self.selectedBots[i % len(self.selectedBots)])
            bot.x , bot.y = self.objects.generationXY()
            bot.alive = True
            bot.Isee = "NONE"
            bot.health = BOT_START_HEALTH
            bot.step = 0
            bot.index = 0
            bot.age = 0
            self.objects.bots.append(bot)
            print("bot append", i)
        selectedBots = []
        print(len(self.objects.bots))

    def handle_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE: 
                    self.stopMode = not(self.stopMode)
                    time.sleep(0.1)
                elif event.key == pygame.K_LEFT: 
                    self.FPS -= 10
                    time.sleep(0.05)
                elif event.key == pygame.K_RIGHT: 
                    self.FPS += 10
                    time.sleep(0.05)
                elif event.key == pygame.K_LEFTBRACKET: 
                        self.selectedColor -= 1
                        if self.selectedColor < 0:
                            self.selectedColor = 0
                        time.sleep(0.1)
                elif event.key == pygame.K_RIGHTBRACKET: 
                        self.selectedColor += 1
                        if self.selectedColor >= len(self.colors):
                            self.selectedColor = len(self.colors) - 1
                        time.sleep(0.1)
                elif event.key == pygame.K_c:
                    self.copyBots()
                    time.sleep(0.2)
                elif event.key == pygame.K_v:
                    self.insertBots()
                    time.sleep(1)

    def drawObjects(self):
        for i in self.objects.poison:
            i.draw()
        for i in self.objects.walls:
            i.draw()
        for i in self.objects.bots:
            i.draw()
        for i in self.objects.food:
            i.draw()
        if self.stopMode:
            #print("COLOR")
            pygame.draw.rect(world.window,self.colors[self.selectedColor],(950,(startY + (height + border) * self.mapW) +30,widht,height))

    def drawText(self):
        self.textInput(30,(startY + (height + border) * self.mapW) + 10,"Max age:",(70, 130, 180))
        self.textInput(100,(startY + (height + border) * self.mapW) + 10,str(self.objects.MaxAge),(70, 130, 180))
        self.textInput(38,(startY + (height + border) * self.mapW) + 30,"Max health:",(70, 130, 180))
        self.textInput(100,(startY + (height + border) * self.mapW) + 30,str(self.objects.MaxHealth),(70, 130, 180))
        self.textInput(15,(startY + (height + border) * self.mapW) + 50,"FPS:",(70, 130, 180))
        self.textInput(100,(startY + (height + border) * self.mapW) + 50,str(self.FPS),(70, 130, 180))
        self.textInput(170,(startY + (height + border) * self.mapW) + 30,"World generation:",(70, 130, 180))
        self.textInput(250,(startY + (height + border) * self.mapW) + 30,str(self.generation),(70, 130, 180))
        self.textInput(150,(startY + (height + border) * self.mapW) + 50,"Work time:",(70, 130, 180))
        self.textInput(350,(startY + (height + border) * self.mapW) + 50,str(int(time.time() - self.startTime + self.workTime)),(70, 130, 180))
        if self.stopMode:
            self.textInput(900,(startY + (height + border) * self.mapW) + 10,"STOP MODE",(70, 130, 180))
            self.textInput(900,(startY + (height + border) * self.mapW) + 30,"selected Color:",(70, 130, 180))
            

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

    def save(self):
        if SAVE:
            self.workTime += int(time.time() - world.startTime)
            with open(SAVE_FILE_NAME,mode ='wb') as data:
                savedData = []
                savedData.append(copy.deepcopy(self.objects.bots))
                savedData.append(copy.deepcopy(self.objects.MaxHealth))
                savedData.append(copy.deepcopy(self.objects.MaxAge))
                savedData.append(copy.deepcopy(self.generation))
                savedData.append(copy.deepcopy(self.workTime))

                data.write(cPickle.dumps(savedData))


            print("Data saved")
        else:
            print("Data didn't save")

    def load(self):
        file = open(LOAD_FILE_NAME,mode="rb")
        data = cPickle.loads(file.read())
        #print(data)
        self.objects.bots = data[0]
        self.objects.MaxHealth = data[1]
        self.objects.MaxAge = data[2]
        self.generation = data[3] 
        self.workTime = data[4]

        file.close()
    



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
        if not(LOAD):
            self.generationBots(bots)
        else:
            world.load()
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
        bot.selected = False
        return bot 
        #random.randint
    def generationNewBots(self):
        self.ID = 0
        world.generation += 1
        lenBots = len(self.bots)
        for i in range(lenBots,BOTS_N):
            
                self.bots.append(self.copyBot(i % lenBots))
            
        for j in range(-8,-1,1):
            y = random.randint(0,len(self.bots[0].DNK)-1)
            self.bots[j].DNK[y] = random.randint(0,63)
    

    def updateBots(self):
        print("Update",len(self.bots))
        if len(self.food) < self.MaxFood // 1.2:
            self.generationFood(self.MaxFood - len(self.food))
        if len(self.poison) < self.MaxPoison // 1.2:
            self.generationPioson(self.MaxPoison - len(self.poison))
        if len(self.bots) > 8:
            #print(len(self.bots))
            health = 0
            age = 0
            while self.ID < len(self.bots):
                if (self.bots[self.ID].alive == False or self.bots[self.ID].health <= 0) and len(self.bots) > 8:
                    print("Del BOt" ,int(self.bots[self.ID].alive),self.bots[self.ID].health,self.ID) 
                    del(self.bots[self.ID]) 

                else:
                    #print("BOT DOING")
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
        self.MaxSteps = 30
        self.selected = False
        self.selectedColor = 0

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
        if self.step <= self.MaxSteps:
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

        if self.step <= self.MaxSteps:
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
        #print("Boot Doing")
        for i in range(self.MaxSteps):
            #print("BOOT DOING")
            while self.index >=64:
                self.index -= 64
            #print("LEN DNK ",len(self.DNK))
            do = self.DNK[self.index]
    
            if do in move:
                #print("Move ",do)
                self.move(do)
                break
            elif do in take:
                #print("Take ",do)
                self.take(do)
                break
            elif do in look:
                #print("Look ",do)
                self.look(do)
                break
            elif do in turn:
                #print("turn ",do)
                self.turnAround(do)
                break
            elif do in jump:
                #print("jump ",do)
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
        if self.selected:
            pygame.draw.rect(world.window,self.selectedColor,(self.getRealX(),self.getRealY(),widht,height))
        else:
            pygame.draw.rect(world.window,self.color,(self.getRealX(),self.getRealY(),widht,height))
        world.textInput(self.getRealX() + widht / 2, self.getRealY() + widht / 2,str(self.health),(255,255,255))

    
world = World()
world.objects.generationAll(POISON_N,WALLS_N,BOTS_N,FOOD_N) #poison,walls,bots,food
world.update() 

while world.run:
    world.update()  
    world.stop()
    world.draw()  
    world.objects.updateBots()
    #world.textInput(500,500,"Hello world" , (200,200,200))

pygame.quit()
world.save()