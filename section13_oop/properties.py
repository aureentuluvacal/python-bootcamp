class Human:
  def __init__(self, first, last, age):
    self.first = first
    self.last = last
    self._age = age

  @property
  def age(self):
    return self._age

  @age.setter
  def age(self, value):
    self._age = max([0, value])

  @property
  def full_name(self):
    return f"{self.first} {self.last}"

jane = Human("Jane", "Goodall", 50)
print(jane.age)
jane.age = -10
print(jane.age)
print(jane.full_name)