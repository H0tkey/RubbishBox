import pygame
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

pygame.display.set_caption("Bot's world!")

x = 0
y = 0
xTarget = 0
yTarget = 0

widht = 40
height = 40
speed = 10
step = 5

run = True

while run:
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
        
    
    if xTarget > x and xTarget <= WINDOW_WIDTH - widht:
        x += step
        xTarget -=step
    if xTarget < x and xTarget >= 0:
        x -= step
        xTarget +=step
    if yTarget > y and yTarget <= WINDOW_HEIGHT - height:
        y += step
        yTarget -= step
    if yTarget < y and yTarget >= 0:
        y -= step
        yTarget +=step
    
    if x == WINDOW_WIDTH - widht or x == 0:
        xTarget = x
    
    if y == WINDOW_HEIGHT - height or y == 0:
        yTarget = y
    
    
    window.fill((0,0,0))
    pygame.draw.rect(window,(0,0,255),(x,y,widht,height))
    pygame.display.update()
    pygame.time.delay(10)
    
    
pygame.quit()
