import pygame 

pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
background_image = pygame.image.load("images/background.jpg")

while True:
    screen.blit(background_image,(0,0))
    pygame.display.update()
    clock.tick(60)