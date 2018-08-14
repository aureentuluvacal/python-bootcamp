import jsonpickle

class Animal:
  def __init__(self, name, species):
    self.name = name
    self.species = species

  def __repr__(self):
    return f"{self.name} is a {self.species}"

pig = Animal("Bacon", "pig")

# with open("pig.json", "w") as file:
#   frozen = jsonpickle.encode(pig)
#   file.write(frozen)

with open("pig.json", "r") as file:
  contents = file.read()
  unfrozen = jsonpickle.decode(contents)
  print(unfrozen)
