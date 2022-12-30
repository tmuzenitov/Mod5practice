import random

class Warrior:
	def __init__(self, name, health = 100):
		self.name = name
		self.health = health

	def hit(self, target):
		if type(self) == type (target):
			target.health -= 20
		else:
			raise TypeError

units = [Warrior('Safana'), Warrior('Ulcaster')]
while True:
	i = random.randint(0, 1)
	attacker, victim = units[i], units[i - 1]
	attacker.hit(victim)
	print(attacker.name, 'hit', victim.name)
	print(victim.name, 'HP ', victim.health)
	if victim.health <= 0:
		print(victim.name, 'died', attacker.name, 'has won')
		break
