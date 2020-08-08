import pygame
import os

class Ship():
	def __init__(self, x, y, vel, health=100):
		self.x = x
		self.y = y
		self.vel = vel
		self.health = health
		self.ship_img = None
		self.laser_img = None
		self.lasers = []
		self.cool_down_counter = 0

	def draw(self, window):
		window.blit(self.ship_img, (self.x, self.y))

	def get_width(self):
		return self.ship_img.get_width()

	def get_height(self):
		return self.ship_img.get_height()


class Player(Ship):
	# player ship and laser 
	YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("images", "pixel_ship_yellow.png"))
	YELLOW_LASER = pygame.image.load(os.path.join("images", "pixel_laser_yellow.png"))
	
	def __init__(self, x, y, vel, health=100):
		super().__init__(x, y, vel, health)
		self.ship_img = self.YELLOW_SPACE_SHIP
		self.laser_img = self.YELLOW_LASER
		self.mask = pygame.mask.from_surface(self.ship_img)
		self.max_health = health





class Enemy(Ship):
	# load images
	RED_SPACE_SHIP = pygame.image.load(os.path.join("images", "pixel_ship_red_small.png"))
	GREEN_SPACE_SHIP = pygame.image.load(os.path.join("images", "pixel_ship_green_small.png"))
	BLUE_SPACE_SHIP = pygame.image.load(os.path.join("images", "pixel_ship_blue_small.png"))
	# lasers 
	RED_LASER = pygame.image.load(os.path.join("images", "pixel_laser_red.png")) 
	GREEN_LASER = pygame.image.load(os.path.join("images", "pixel_laser_green.png"))
	BLUE_LASER = pygame.image.load(os.path.join("images", "pixel_laser_blue.png"))
	
	COLOR_MAP = {
		"red": (RED_SPACE_SHIP, RED_LASER),
		"green": (GREEN_SPACE_SHIP, GREEN_LASER),
		"blue": (BLUE_SPACE_SHIP, BLUE_LASER)
	}

	def __init__(self, x, y, vel, color, health=100):
		super().__init__(x, y, vel, health)
		self.ship_img, self.laser_img = self.COLOR_MAP[color]
		self.mask = pygame.mask.from_surface(self.ship_img)

	def move(self):
		self.y += self.vel