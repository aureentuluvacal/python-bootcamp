from copy import copy

class Human:
  def __init__(self, first, last, age):
    self.first = first
    self.last = last
    self.age = age

  def __repr__(self):
    return f"Human named {self.first} {self.last}"

  def __len__(self):
    return self.age

  def __add__(self, other):
    if isinstance(other, Human):
      return Dog("Lolita", "Pita")

    raise TypeError(f"Expecting {type(self)}, received {type(other)}")

  def __mul__(self, other):
    if isinstance(other, int):
      return [copy(self) for i in range(other)]
    
    raise TypeError(f"Expecting {type(1)}, received {type(other)}")


class Animal:
  def __init__(self, name, species):
    self.name = name
    self.species = species

class Dog(Animal):
  def __init__(self, name, nickname):
    super().__init__(name, species = "Dog")
    self.nickname = nickname

  def __repr__(self):
    return f"A Dog named {self.name} ({self.nickname})"

i = Human("Irma", "Mesa", 25)
c = Human("Caryssa", "Perez", 24)
print(i)
print(len(i))

print(i + c)
mesas = i * 2
mesas[1].first = "Stephanie"
print(mesas)
print(i * c)
