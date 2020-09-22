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
		self.new_line = True
		self.side_move_to = 99

	def move(self, d_width, d_height):
		
		if self.new_line:
			self.begin_train(d_width, d_height)
			self.new_line = False
		else:
			if self.side_move_to == 0:
				self.pos_y += self.speed
				if self.pos_y > d_height:
					self.new_line = True
			elif self.side_move_to == 1:
				self.pos_y -= self.speed
				if self.pos_y < 0:
					self.new_line = True
			elif self.side_move_to == 2:
				self.pos_x += self.speed
				if self.pos_x > d_width:
					self.new_line = True
			elif self.side_move_to == 3:
				self.pos_x -= self.speed
				if self.pos_x < 0:
					self.new_line = True
			print(self.side_move_to)
			print(self.pos_x)
		pygame.draw.rect(self.display, self.color, (self.pos_x, self.pos_y, self.width, self.height))
	def begin_train(self, d_width, d_height):
		start_side = random.randrange(0, 4)
		
		if start_side == 0:
			self.pos_x = random.randrange(0, d_width - self.height)
			self.pos_y = 0 - self.height - 100
			self.side_move_to = 0
		elif start_side == 1:
			self.pos_x = random.randrange(0, d_width - self.height)
			self.pos_y = d_height + self.height + 100
			self.side_move_to = 1
		elif start_side == 2:
			self.pos_y = random.randrange(0, d_height - self.height)
			self.pos_x = 0 - self.width - 100
			self.side_move_to = 2
		elif start_side == 3:
			self.pos_y = random.randrange(0, d_height - self.height)
			self.pos_x = 0 - self.width - 100
			self.side_move_to = 3
		self.height = random.randrange(50, 500, 20)
		self.color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
		self.speed = random.randrange(2, 10)
		print('lol')
		
		
def user_events(pos_x, pos_y, speed, display_width, display_height):
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	keys = pygame.key.get_pressed()

	if keys[pygame.K_w]:
		pos_y -=speed
	if keys[pygame.K_s]:
		pos_y += speed
	if keys[pygame.K_a]:
		pos_x -= speed
	if keys[pygame.K_d]:
		pos_x += speed	
		
	if pos_x > display_width-30:
		pos_x = display_width-30
	if pos_x < 0:
		pos_x = 0
	if pos_y > display_height - 30:
		pos_y = display_height - 30
	if pos_y < 0:
		pos_y = 0
	return pos_x, pos_y
