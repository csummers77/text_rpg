import random
import os

class Zombie():
	def __init__(self, health, zombie_power, weapon):
		self.health = health
		self.power = zombie_power
		self.weapon = weapon
zombie_health = 100
zombie_power = 100
zombie_currentWeapon = True
hasWeapon = False

zombieWeapon = {
	"firstWeapon": "baseball-bat",
	"secondWeapon": "nail-bat",
	"thirdWeapon": "hammer"
}
zombie = Zombie(100, 100, zombieWeapon["firstWeapon"])
print 