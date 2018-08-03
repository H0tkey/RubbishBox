import pygame
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


pygame.init()

clock = pygame.time.Clock()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("Bot's world'!")

x = 1
y = 1
xTarget = x
yTarget = y

widht = 24
height = 24
border = 2
speed = 1


run = True

Map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
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
    def __init__(self, x, y, health):
        self.x = x
        self.y = y
        self.xTarget = x
        self.yTarget = y
        self.index = 0
        self.step = 0
        self.health = height
        self.DNK = getArray(32)

    def draw(self):
        pass

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


bot = Bot(1, 1, 40)


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

    if bot.xTarget > bot.x:
        bot.goLeft()
    if bot.xTarget < bot.x:
        bot.goRight()
    if bot.yTarget > bot.y:
        bot.goDown()
    if bot.yTarget < bot.y:
        bot.goUp()


while run:

    clock.tick(30)
    handle_events()
    update()
    drawWindow()


pygame.quit()
