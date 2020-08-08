import time
import random
import utilities
from utilities import pygame, collide

pygame.font.init()

# window
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sapce Invaders")

# background
BG = pygame.transform.scale(pygame.image.load(utilities.os.path.join("images", "background-black.png")), (WIDTH, HEIGHT))


def main():

	# variables
	run = True
	FPS = 60
	level = 0
	lives = 5
	main_font = pygame.font.SysFont("comicsans", 50)
	lost_font = pygame.font.SysFont("magnito", 60)
	player_vel = 5
	lost = False
	lost_count = 0

	laser_vel = 5

	enemies = []
	wave_length = 0
	enemy_vel = 1

	player = utilities.Player(300, 630, player_vel)

	clock = pygame.time.Clock()

	def redraw_window():
		WIN.blit(BG, (0, 0))
		# draw text
		lives_label = main_font.render(f"lives: {lives}", 1, (255,255,255))
		level_label = main_font.render(f"level: {level}", 1, (255,255,255))
		
		WIN.blit(lives_label, (10, 10))
		WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
		
		for enemy in enemies:
			enemy.draw(WIN)

		player.draw(WIN)

		if lost:
			lost_label = lost_font.render("You Lost!!", 1, (255,255,255))
			WIN.blit(lost_label, (WIDTH//2 - lost_label.get_width()//2, 350))

		pygame.display.update()

	while run:
		clock.tick(FPS)
		redraw_window()

		# loss
		if lives < 0 or player.health <= 0:
			lost = True
			lost_count += 1
		
		if lost:
			if lost_count > FPS * 5:
				run = False
			else:
				continue

		# enemy 
		if not enemies:
			level += 1
			wave_length += 5
			for i in range(wave_length):
				enemy = utilities.Enemy(random.randrange(50, WIDTH-50), random.randrange(-1500, -100), enemy_vel, random.choice(["red", "green", "blue"]))
				enemies.append(enemy)
		for enemy in enemies[:]:
			enemy.move()
			enemy.move_lasers(laser_vel, player, HEIGHT)

			if random.randrange(0, 2*FPS) == 1:
				enemy.shoot()

			if collide(enemy, player):
				player.health -= 10
				enemies.remove(enemy)
			elif enemy.y + enemy.get_height() > HEIGHT:
				lives -= 1
				enemies.remove(enemy)

		# player
		player.move_lasers(-laser_vel, enemies, HEIGHT)

		# events 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()

		# key presses 
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:
			player.shoot()
		if keys[pygame.K_a] and player.x - player.vel > 0: #left
			player.x -= player.vel
		if keys[pygame.K_d] and player.x + player.vel + player.get_width() < WIDTH: #right
			player.x += player.vel
		if keys[pygame.K_w] and player.y - player.vel > 0: #up
			player.y -= player.vel
		if keys[pygame.K_s] and player.y + player.vel + player.get_height() + 15 < HEIGHT: #down
			player.y += player.vel

def main_menu():
	title_font = pygame.font.SysFont("comicsans", 70)
	run = True
	while run:
		WIN.blit(BG, (0,0))
		title_label = title_font.render("Press the mouse to begin...", 1, (255,255,255))
		WIN.blit(title_label, (WIDTH//2 - title_label.get_width()//2, 350))
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				main()
	pygame.quit()

main_menu()