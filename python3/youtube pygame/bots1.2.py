import pygame
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


pygame.init()

clock = pygame.time.Clock()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("Bot's world'!")

#x = 2
#y = 2
#xTarget = x
#yTarget = y

up = [0,1,2]
down = [6,5,4]
left = [0,7,6]
right = [2,3,4]



widht = 24
height = 24
border = 2
speed = 1
botID = 0

run = True

Map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
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
        Map[y][x] = 2
        self.xTarget = x
        self.yTarget = y
        self.act = 0
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
        global xTarget,yTarget
        sell = self.DNK[self.index]
        if sell <= 7:
            if sell == 0:
                xTarget -= 1
                yTarget -= 1
            if sell == 2:
                xTarget -= 1

    def move(self,n):
        self.health -= 1
        self.act = 'move'
        command = n + self.direction
        if command > 7 :
            command -= 8
        if command in up:
            self.yTarget -=1
        if command in down:
            self.yTarget +=1
        if command in left:
            self.xTarget -=1
        if command in right:
            print("ok")
            self.xTarget +=1

    def take(self,n):
        self.act = 'take'
        command = n + self.direction - 8
        if command > 7 :
            command -= 8
        if command in up:
            self.yTarget -=1
        if command in down:
            self.yTarget +=1
        if command in left:
            self.xTarget -=1
        if command in right:
            print("ok")
            self.xTarget +=1

    def look(self,n):
        self.act = 'look'
        command = n + self.direction - 8*2
        if command > 7 :
            command -= 8
        if command in up:
            self.yTarget -=1
        if command in down:
            self.yTarget +=1
        if command in left:
            self.xTarget -=1
        if command in right:
            print("ok")
            self.xTarget +=1

    def turnAround(self,n):
        self.act = 'turn'
        command = n + self.direction - 8*3
        if command > 7 :
            command -= 8
        if command in up:
            self.yTarget -=1
        if command in down:
            self.yTarget +=1
        if command in left:
            self.xTarget -=1
        if command in right:
            print("ok")
            self.xTarget +=1



    def goLeft(self):
        global Map
        if self.xTarget < len(Map[0]) - 1:
            self.x += 1
            Map[self.y][self.x], Map[self.y][self.x -
                                             1] = Map[self.y][self.x - 1], 0

    def goRight(self):
        global Map
        if self.xTarget > 0:
            self.x -= 1
            Map[self.y][self.x], Map[self.y][self.x +
                                             1] = Map[self.y][self.x + 1], 0

    def goDown(self):
        global Map
        if self.yTarget < len(Map) - 1:
            self.y += 1
            Map[self.y][self.x], Map[self.y -
                                     1][self.x] = Map[self.y - 1][self.x], 0

    def goUp(self):
        global Map
        if self.yTarget > 0:
            self.y -= 1
            Map[self.y][self.x], Map[self.y +
                                     1][self.x] = Map[self.y + 1][self.x], 0

    def take(self):



bot = Bot(10, 10, 40,6)


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

    global bot, run

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        bot.xTarget -= speed
    if keys[pygame.K_RIGHT]:
        bot.xTarget += speed

    if keys[pygame.K_UP]:
        bot.yTarget -= speed
    if keys[pygame.K_DOWN]:
        bot.yTarget += speed


def update():

    if bot.act == 'move': 
        if bot.xTarget > bot.x:
            bot.goLeft()
        if bot.xTarget < bot.x:
            bot.goRight()
        if bot.yTarget > bot.y:
            bot.goDown()
        if bot.yTarget < bot.y:
            bot.goUp()

    if bot.act == 'take': 

n = 0
while run:

    clock.tick(30)
    bot.move(n)
    handle_events()
    update()
    print(bot.health)
    drawWindow()
    n += 1
    if n == 8:
        n = 0

pygame.quit()
