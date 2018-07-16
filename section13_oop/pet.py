class Pet:

  permitted_species = ("cat", "dog", "bearded dragon")

  def __init__(self, name, species):
    if species not in Pet.permitted_species:
      raise ValueError(f"You can't have a {species}")

    self.name = name
    self.species = species

  def set_species(self, species):
    if species not in Pet.permitted_species:
      raise ValueError(f"You can't have a {species}")

    self.species = species

cat = Pet("Blue", "cat")
cat.set_species("tiger")