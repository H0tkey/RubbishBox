import pygame

pygame.init()
window = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Cubes Game")

x = 50
y = 50
widht = 40
height = 60
speed = 5
run = True


while run:

for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

		#pygame.draw.rectangle(window,x,y,widht,height)
		pygame.display.update()
		pygame.time.delay(10)


pygame.quit()
