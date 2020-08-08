import time
import random
import utilities
from utilities import pygame

pygame.font.init()

# window
WIDTH, HEIGHT = 650, 650
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sapce Invaders")

# background
BG = pygame.transform.scale(pygame.image.load(utilities.os.path.join("images", "background-black.png")), (WIDTH, HEIGHT))


def main():
	run = True
	FPS = 60
	level = 1
	lives = 5
	main_font = pygame.font.SysFont("comicsans", 30)

	enemies = []

	player = utilities.Player(200, 550, 5)

	clock = pygame.time.Clock()

	def redraw_window():
		WIN.blit(BG, (0, 0))
		# draw text
		lives_label = main_font.render(f"lives: {lives}", 1, (255,255,255))
		level_label = main_font.render(f"level: {level}", 1, (255,255,255))
		
		WIN.blit(lives_label, (10, 10))
		WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))


		player.draw(WIN)

		pygame.display.update()

	while run:
		clock.tick(FPS)
		redraw_window()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		keys = pygame.key.get_pressed()
		if keys[pygame.K_a] and player.x - player.vel > 0: #left
			player.x -= player.vel
		if keys[pygame.K_d] and player.x + player.vel + player.get_width() < WIDTH: #right
			player.x += player.vel
		if keys[pygame.K_w] and player.y - player.vel > 0: #up
			player.y -= player.vel
		if keys[pygame.K_s] and player.y + player.vel + player.get_height() < HEIGHT: #down
			player.y += player.vel
main()