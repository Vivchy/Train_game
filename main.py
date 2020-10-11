import pygame 
import area

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
	train = area.Train(display, 50, 150, 10, 20, 100)
	train2 = area.Train(display, 50, 150, 10, 20, 100)
	train3 = area.Train(display, 50, 150, 10, 20, 100)
	train4 = area.Train(display, 50, 150, 10, 20, 100)
	trains = [train, train2, train3, train4]

	while True:
		pos_x, pos_y = area.user_events(pos_x, pos_y, speed, display_width, display_height)
		
		display.fill((222, 222, 222))
		pygame.draw.rect(display, (0, 0, 0), (pos_x, pos_y, 30, 30))
		
		trains[0].move(display_width, display_height)
		trains[1].move(display_width, display_height)
		trains[2].move(display_width, display_height)
		trains[3].move(display_width, display_height)
		for train in trains:
			if pos_x + 30 > train.pos_x and pos_x < train.pos_x + train.width:
				if pos_y + 30 > train.pos_y and pos_y < train.pos_y + train.height:
					print(pos_y)
		pygame.display.update()
		clock.tick(60)
run_game()

