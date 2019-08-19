class Kettle(object):

  power_source = "eletricity"

  def __init__(self, make, price):
    self.make = make
    self.price = price
    self.on = False

  def switch_on(self):
    self.on = True

kenwood = Kettle("Kenwood", 8.99)
hamilton = Kettle("Hamilton", 14.55)

print(kenwood.make)
print(kenwood.price)
kenwood.price = 12.75
print(kenwood.price)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

print(">" * 40)

print(kenwood.on)
Kettle.switch_on(kenwood)
print(kenwood.on)

print(">" * 40)

kenwood.power = 1.5
print(kenwood.power)

print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
Kettle.power_source = "atomic"
print("Switch Kettle to atomic")
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
kenwood.power_source = "gas"
print("Switch kenwood to gas")
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)

print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)