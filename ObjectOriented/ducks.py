class Wing(object):

  def __init__(self, ratio):
    self.ratio = ratio

  def fly(self):
    if self.ratio > 1:
      print("Weee, this is fun")
    elif self.ratio == 1:
      print("This is hard work, but I am flying")
    else:
      print("I think I'll just walk")

class Duck(object):

  def __init__(self):
    self._wing = Wing(1.8)

  def walk(self):
    print("Waddle, waddle, waddle")

  def swim(self):
    print("Splish, splash")

  def talk(self):
    print("Quack quack")
  
  def fly(self):
    self._wing.fly()

class Penguim(object):

  def walk(self):
    print("Waddle, waddle, I waddle too")

  def swim(self):
    print("Splish, splash, chilly")

  def talk(self):
    print("Peep peep")

# def test_duck(duck):
#   duck.walk()
#   duck.swim()
#   duck.talk()

if __name__ == '__main__':
  donald = Duck()
  donald.fly()