import pygame
import random
class Train():
	def __init__(self, display, width, height, speed, pos_x, pos_y):
		self.width = width
		self.height = height
		self.speed = speed
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.start_p = pos_y
		self.color = (0, 0, 0)
		self.display = display

	def move(self, d_width):
		pygame.draw.rect(self.display, self.color, (self.pos_x, self.pos_y, self.width, self.height))
		self.pos_y += self.speed
		if self.pos_y > 600:
			self.pos_y = -self.height
			self.pos_x = random.randrange(self.width, d_width - self.width)
			self.height = random.randrange(50, 500, 20)
			self.color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
			self.speed = random.randrange(2, 20)

