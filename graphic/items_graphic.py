import pygame
from logic import constants

class ItemsDisplay:
	def __init__(self, hero, items_to_display):
		self.hero = hero
		self.items_to_display = items_to_display
		self.picked_items = []
		
	def display(self, display):
		for item in self.items_to_display:
			if [item.x, item.y] != [self.hero.x, self.hero.y]:
				constants.SCREEN.blit(pygame.transform.scale(pygame.image.load(str(item.image)), (constants.SPRITE_SIZE,constants.SPRITE_SIZE)),(item.x, item.y))
			else:
				self.items_to_display.remove(item)
				self.picked_items.append(item)
		for item in self.picked_items:
			constants.SCREEN.blit(pygame.transform.scale(pygame.image.load(str(item.image)), (constants.SPRITE_SIZE, constants.SPRITE_SIZE)),(17 * constants.SPRITE_SIZE, (constants.SPRITE_SIZE * (4 + 2 * self.picked_items.index(item)))))
