import pygame
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


pygame.init()

clock = pygame.time.Clock()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

pygame.display.set_caption("Bot's world'!")

x = 5
y = 5
xTarget = x
yTarget = y

widht = 25
height = 25
border = 5
speed = 15
step = 30

run = True

Map = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]


def drawWindow():
    
    startX = 5 
    startY = 5
        
    global Map
    
    window.fill((230, 230, 250))
    
    #for line in range(len(Map)):
        #for sell in range(len(Map[line])):
            #pygame.draw.rect(window,(100,100,100),(startX + (widht + border) * sell,startY + (height + border) * line,widht,height))
            
    
    pygame.draw.rect(window,(0,0,255),(x,y,widht,height))
    pygame.display.update()
    

def handle_events():
    
    global xTarget,yTarget,run
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: 
        xTarget -= speed 
    if keys[pygame.K_RIGHT]:
        xTarget += speed 
    
    if keys[pygame.K_UP]:
        yTarget -= speed 
    if keys[pygame.K_DOWN]:
        yTarget += speed 
        
    

def update():
    
    global x, y, xTarget, yTarget
    
    if x != xTarget:
        if xTarget > x and xTarget <= WINDOW_WIDTH - widht:
            x += step
            xTarget -=step
            print("ok")
        if xTarget < x and xTarget >= 5:
            x -= step
            xTarget +=step
    if y != yTarget:
        if yTarget > y and yTarget <= WINDOW_HEIGHT - height:
            y += step
            yTarget -= step
        if yTarget < y and yTarget >= 5:
            y -= step
            yTarget +=step
        
    if x == WINDOW_WIDTH - widht or x == 5:
        xTarget = x
    
    if y == WINDOW_HEIGHT - height or y == 5:
        yTarget = y

    


while run:
    
    clock.tick(30)
    handle_events()
    update()
    drawWindow()
    #print(x,xTarget)
    #print(y,yTarget)
    
    
pygame.quit()
