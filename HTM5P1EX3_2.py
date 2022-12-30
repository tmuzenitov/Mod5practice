import random

class Warrior:
  def __init__(self, name, health = 100, endurance = 100, armor = 100):
    self.name = name
    self.health = health
    self.end = endurance
    self.armor = armor


  def hit(self, target):
    if type(self) == type (target) and self.end > 0 and target.armor > 0:
      target.health -= 0.20
      target.armor -= 0.10
      self.end -= 10
      
      

units = [Warrior('Safana'), Warrior('Ulcaster')]
while True:
  i = random.randint(0, 1)
  attacker, victim = units[i], units[i - 1]
  attacker.hit(victim)
  print(attacker.name, 'hit', victim.name, 'Endurance left', attacker.end)
  print(victim.name, 'HP ', victim.health, 'Armor', victim.armor)
  if victim.health <= 0:
    print(victim.name, 'died', attacker.name, 'is the winner')
    break
