import json

class Animal:
  def __init__(self, name, species):
    self.name = name
    self.species = species

  def __repr__(self):
    return f"{self.name} is a {self.species}"

j = json.dumps(['foo', {'bar': 'baz'}])
pig = Animal("Bacon", "pig")
pig_json = json.dumps(pig.__dict__)

print(j)
print(pig_json)
