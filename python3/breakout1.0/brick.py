import pygame

from game_object import GamaObject
class Brick(GamaObject):
	def __init__(self,x,y,w,h,color,special_effect=None):
		GamaObject.__init__(self,x,y,w,h)
		self.color = color
		self.special_effect = special_effect

	def draw(self,surface):
		pygame.draw.rect(surface,self.color,self.bounds)