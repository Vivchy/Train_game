import pygame 

pygame.init()
display_width = 600
display_height = 500
display = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
def run_game():
	""" Основной цикл игры"""
	pos_x = 300
	pos_y = 250
	speed = 10
	motion = 'STOP'
	while True:
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
		#аналог по остальным сторнам		
		if pos_x > display_width-30:
			pos_x = display_width-30
		if pos_x < 0:
			pos_x = 0
		if pos_y > display_height - 30:
			pos_y = display_height - 30
		if pos_y < 0:
			pos_y = 0
		display.fill((222, 222, 222))
		pygame.draw.rect(display, (0, 0, 0), (pos_x, pos_y, 30, 30))

		pygame.display.update()
		clock.tick(60)
run_game()

