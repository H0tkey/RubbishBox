import pygame
from text_object import *
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


pygame.init()

clock = pygame.time.Clock()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("Bots's world'!")

#x = 2
#y = 2
#xTarget = x
#yTarget = y

up = [0, 1, 2]
down = [6, 5, 4]
left = [0, 7, 6]
right = [2, 3, 4]


widht = 24
height = 24
border = 2
speed = 1
ID = 0

run = True

Map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 4, 0, 1],
       [1, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 4, 0, 1],
       [1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 1],
       [1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 4, 0, 0, 4, 0, 1],
       [1, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 1],
       [1, 0, 3, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 0, 4, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 0, 4, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


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
        print(self.x,self.y)
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

population = []
population.append(Bot(10, 10, 10, 2))
population.append(Bot(1, 4, 10, 2))
population.append(Bot(4, 12, 10, 2))
population.append(Bot(12, 10, 10, 2))
population.append(Bot(12, 12, 10, 2))
population.append(Bot(1, 4, 10, 2))
population.append(Bot(4, 16, 10, 2))
population.append(Bot(15, 4, 10, 2))
population.append(Bot(15, 12, 10, 2))

#population[ID] = 


def getColor(color):
    if color == 0:  # EMPTY
        return (192, 192, 192)
    if color == 1:  # WAll
        return (128, 128, 128)
    if color == 2:  # population[ID]
        return (0, 0, 128)
    if color == 3:  # FOOD
        return (50, 205, 50)
    if color == 4:  # POISON
        return (139, 0, 0)
    if color == 5:  # CORPSE
        return (224, 255, 255)


def drawWindow():

    startX = 5
    startY = 5

    global Map

    window.fill((240, 240, 250))

    for line in range(len(Map)):
        for sell in range(len(Map[line])):
            pygame.draw.rect(window, (getColor(Map[line][sell])), (startX + (
                widht + border) * sell, startY + (height + border) * line, widht, height))

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
    global population , Map, ID
    if population[ID].alive and population[ID].health != 0: 
        if population[ID].act == 'move':
            if Map[population[ID].yTarget][population[ID].xTarget] == 0:  # EMPTY
                population[ID].Isee = 0
                population[ID].go()
                ID += 1
            elif Map[population[ID].yTarget][population[ID].xTarget] == 1:  # Wall
                population[ID].Isee = 1
                population[ID].xTarget = population[ID].x
                population[ID].yTarget = population[ID].y
                ID += 1
            elif Map[population[ID].yTarget][population[ID].xTarget] == 2:  # BOT
                population[ID].Isee = 2
                population[ID].xTarget = population[ID].x
                population[ID].yTarget = population[ID].y
                ID += 1
            elif Map[population[ID].yTarget][population[ID].xTarget] == 3:  # FOOD
                population[ID].Isee = 3
                population[ID].health += 20
                population[ID].go()
                ID += 1
            elif Map[population[ID].yTarget][population[ID].xTarget] == 4:  # POISON
                population[ID].Isee = 4
                population[ID].alive = False
                population[ID].go()
                ID += 1
            elif Map[population[ID].yTarget][population[ID].xTarget] == 5:  # CORPSE
                population[ID].Isee = 5
                population[ID].xTarget = population[ID].x
                population[ID].yTarget = population[ID].y
                ID += 1

        elif population[ID].act == 'take':
            if Map[population[ID].yTarget][population[ID].xTarget] == 0:  # EMPTY
                population[ID].Isee = 0
                population[ID].xTarget = population[ID].x
                population[ID].yTarget = population[ID].y
                ID += 1
            elif Map[population[ID].yTarget][population[ID].xTarget] == 1:  # Wall
                population[ID].Isee = 1
                population[ID].xTarget = population[ID].x
                population[ID].yTarget = population[ID].y
                ID += 1
            elif Map[population[ID].yTarget][population[ID].xTarget] == 2:  # BOT
                population[ID].Isee = 2
                population[ID].xTarget = population[ID].x
                population[ID].yTarget = population[ID].y
                ID += 1
            elif Map[population[ID].yTarget][population[ID].xTarget] == 3:  # FOOD
                population[ID].Isee = 3
                population[ID].health += 50
                
                ID += 1
                Map[population[ID].yTarget][population[ID].xTarget] = 0
                population[ID].xTarget = population[ID].x
                population[ID].yTarget = population[ID].y
            elif Map[population[ID].yTarget][population[ID].xTarget] == 4:  # POISON
                population[ID].Isee = 4
                ID += 1
                Map[population[ID].yTarget][population[ID].xTarget] = 3
                population[ID].xTarget = population[ID].x
                population[ID].yTarget = population[ID].y
            elif Map[population[ID].yTarget][population[ID].xTarget] == 5:  # CORPSE
                population[ID].Isee = 5
                population[ID].xTarget = population[ID].x
                population[ID].yTarget = population[ID].y
                ID += 1
        elif population[ID].act == 'look':
            if Map[population[ID].yTarget][population[ID].xTarget] == 0:  # EMPTY
                population[ID].Isee = 0
                population[ID].xTarget = population[ID].x
                population[ID].yTarget = population[ID].y
    
            elif Map[population[ID].yTarget][population[ID].xTarget] == 1:  # Wall
                population[ID].Isee = 1
                population[ID].xTarget = population[ID].x
                population[ID].yTarget = population[ID].y
                
            elif Map[population[ID].yTarget][population[ID].xTarget] == 2:  # BOT
                population[ID].Isee = 2
                population[ID].xTarget = population[ID].x
                population[ID].yTarget = population[ID].y
                
            elif Map[population[ID].yTarget][population[ID].xTarget] == 3:  # FOOD
                population[ID].Isee = 3
                population[ID].xTarget = population[ID].x
                population[ID].yTarget = population[ID].y
            elif Map[population[ID].yTarget][population[ID].xTarget] == 4:  # POISON
                population[ID].Isee = 4
                population[ID].xTarget = population[ID].x
                population[ID].yTarget = population[ID].y
            elif Map[population[ID].yTarget][population[ID].xTarget] == 5:  # CORPSE
                population[ID].Isee = 5
                population[ID].xTarget = population[ID].x
                population[ID].yTarget = population[ID].y

    else:
        del(population[ID])


#def textF():
 #   message = TextObject(700,700, lambda: "gdhdhd", (200,200,200), 'Arial', 20)
  #  #draw()
   # message.draw(self.surface, centralized)

n = 0
drawWindow()
pygame.time.delay(1000)
while run:

    clock.tick(30)
    population[ID].move(n)
    handle_events()
    update()
    #textF()
    if len(population) == 0:
        break
    drawWindow()
    n += 1
    if n == 8:
        n = 0
    if ID >= len(population):
        ID = 0

    print(ID,population[ID].health)
pygame.quit()
