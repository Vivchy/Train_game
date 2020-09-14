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
	motion = 'STOP'
	while True:
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				
		display.fill((222, 222, 222))
		pygame.draw.rect(display, (0, 0, 0), (pos_x, pos_y, 30, 30))

		pygame.display.update()
		clock.tick(60)
run_game()

