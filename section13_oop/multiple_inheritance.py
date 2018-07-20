class Aquatic:
  def __init__(self, name):
    self.name = name

  def swim(self):
    return f"{self.name} is swimming"

  def greet(self):
    return f"I am {self.name} of the sea!"

class Ambulatory:
  def __init__(self, name):
    self.name = name

  def walk(self):
    return f"{self.name} is walking"

  def greet(self):
    return f"I am {self.name} of the land!"

# Penguin will trigger the Ambulatory methods because 
# it is the first position based on method resolution # order (MRO)
class Penguin(Ambulatory, Aquatic):
  def __init__(self, name):
    super().__init__(name=name)

kraken = Aquatic("Kraken")
schnookums = Ambulatory("Schnookums")
penguin = Penguin("Pengo")

print(penguin.swim())
print(penguin.walk())
print(penguin.greet())

# Print MRO, can use mro() or help(Class)
print(Penguin.__mro__)