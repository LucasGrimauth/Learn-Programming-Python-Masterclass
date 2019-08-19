class Enemy:

  def __init__(self, name="Enemy", hp=0, lives=1):
    self._name = name
    self._hp = hp
    self._lives = lives
    self._alive = True
  
  def take_damage(self, damage):
    remaining_hp = self._hp - damage
    if remaining_hp >= 0:
      self._hp = remaining_hp
      print("{0._name} took {1} damage and have {0._hp} hp left".format(self, damage))
    else:
      self._lives -= 1
      if self._lives > 0:
        print("{0._name} lost a life".format(self))
      else:
        print("{0._name} was slain".format(self))
        self._alive = False

  def __str__(self):
    return "Name: {0._name}, Lives: {0._lives}, HP: {0._hp}".format(self)

# Troll enemy
class Troll(Enemy):

  def __init__(self, name):
    # super(Troll, self).__init__(self, name=name, hp=23, lives=1)
    super().__init__(name=name, hp=23, lives=1)

  def grunt(self):
    print("Me {0._name}. {0._name} stomp you!".format(self))

# Vampyre enemy
class Vampyre(Enemy):

  def __init__(self, name):
    super().__init__(name=name, hp=12, lives=3)

  def dodges(self):
    import random
    if random.randint(1, 3) == 3:
      if(random.randint(1, 2) == 1):
        print("***** {0._name} turns into a bat and dodges! *****".format(self))
      else:
        print("***** {0._name} swiftly eludes you with his cloak! *****".format(self))
      return True
    else:
      return False

  def take_damage(self, damage):
    if not self.dodges():
      super().take_damage(damage=damage)

# VampyreKing enemy
class VampyreKing(Vampyre):

  def __init__(self, name):
    super().__init__(name=name)
    self._hp = 140
  
  def take_damage(self, damage):
    super().take_damage(damage=damage // 4)

  