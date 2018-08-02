import pygame
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

pygame.display.set_caption("Game!")

walkRight = [pygame.image.load("images/tramp/pygame_right_1.png"),
pygame.image.load("images/tramp/pygame_right_2.png"),
pygame.image.load("images/tramp/pygame_right_3.png"),
pygame.image.load("images/tramp/pygame_right_4.png"),
pygame.image.load("images/tramp/pygame_right_5.png"),
pygame.image.load("images/tramp/pygame_right_6.png")]

walkLeft = [pygame.image.load("images/tramp/pygame_left_1.png"),
pygame.image.load("images/tramp/pygame_left_2.png"),
pygame.image.load("images/tramp/pygame_left_3.png"),
pygame.image.load("images/tramp/pygame_left_4.png"),
pygame.image.load("images/tramp/pygame_left_5.png"),
pygame.image.load("images/tramp/pygame_left_6.png"),]

idle = pygame.image.load("images/tramp/idle.png")
background = pygame.image.load("images/tramp/bg.jpg")

bullets = []

class Bullet():
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
        
    def draw(self,window):
        pygame.draw.circle(window,self.color,(self.x,self.y),self.radius)

x = 0
y= 0
widht = 60
height = 71
speed = 5
isJump = False
jumpLenght = 15
jumpCount = 10

left = False
right = False
animCount = 0
lastMove = "right"

clock = pygame.time.Clock()

def drawWindow():
    global animCount
    window.blit(background,(0,0))
    if animCount +1 >= 30:
        animCount = 0
        
    if left:
        window.blit(walkLeft[animCount //5],(x,y))
        animCount += 1
    elif right:
        window.blit(walkRight[animCount //5],(x,y))
        animCount += 1
    else:
        window.blit(idle,(x,y))
    
    for bullet in bullets:
        bullet.draw(window)
    
    #pygame.draw.rect(window,(0,0,255),(x,y,widht,height))
    pygame.display.update()
    

run = True

while run:
    
    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    for bullet in bullets:
        if bullet.x < WINDOW_WIDTH and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_f]:
        if lastMove == "right":
            facing = 1
        else:
            facing = -1
        
        if len(bullets) < 5:
            bullets.append(Bullet(round(x + widht // 2),round(y + height // 2),
            5,(255,0,0),facing))
    
    if keys[pygame.K_LEFT] and x > 0: 
        x -= speed 
        left = True
        right = False
        lastMove = 'left'
    elif keys[pygame.K_RIGHT] and x < WINDOW_WIDTH - widht:
        x += speed 
        left = False
        right = True
        lastMove = 'right'
    else:
        left = False
        right = False
        animCount = 0
        
    if not(isJump):
        if keys[pygame.K_UP] and y > 0:
            y -= speed 
        if keys[pygame.K_DOWN] and y < WINDOW_HEIGHT - height:
            y += speed 
            
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            y -= jumpCount*2
            jumpCount-=1
        else:
            isJump = False
            jumpCount = 10
    
    drawWindow()
    
    
pygame.quit()
