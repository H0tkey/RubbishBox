import pygame

pygame.init()
window = pygame.display.set_mode((800,600))

pygame.display.set_caption("Game!")

x = 50
y= 60
widht = 40
height = 40
speed = 5
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed 
    if keys[pygame.K_RIGHT]:
        x += speed 
    
    if keys[pygame.K_UP]:
        y -= speed 
    if keys[pygame.K_DOWN]:
        y += speed 
    
    
    
    pygame.draw.rect(window,(0,0,255),(x,y,widht,height))
    pygame.display.update()
    pygame.time.delay(10)
    
    
pygame.quit()
