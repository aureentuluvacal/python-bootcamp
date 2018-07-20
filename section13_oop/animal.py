class Animal:
  def __init__(self, name, species):
    self.name = name
    self.species = species

  def __repr__(self):
    return f"{self.name} is a {self.species}"

class Cat(Animal):
  def __init__(self, name, breed, favorite_toy):
    super().__init__(name, species = "Cat")
    self.breed = breed
    self.favorite_toy = favorite_toy

  def play(self):
    return f"{self.name} plays with {self.favorite_toy}"

schnookums = Cat("Schnookums", "Tabby", "paperclips")
print(schnookums)
print(schnookums.play())