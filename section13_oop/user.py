class User:

  active_users = 0

  def __init__(self, firstname, lastname, age):
    self.firstname = firstname
    self.lastname = lastname
    self.age = age
    User.active_users += 1

  def __repr__(self):
    return f"{self.firstname}"

  def logout(self):
    User.active_users -= 1
    return f"{self.firstname} has logged out"

  def full_name(self):
    return f"{self.firstname} {self.lastname}"
  
  def initials(self):
    return f"{self.firstname[0]}. {self.lastname[0]}."

  def likes(self, thing):
    return f"{self.firstname} likes {thing}"

  @classmethod
  def display_active_users(cls):
    return f"There are currently {cls.active_users} users online."

  @classmethod
  def normalize_arguments(cls, args_str):
    first, last, age = args_str.split(",")
    return cls(first, last, int(age))

class Moderator(User):
  active_mods = 0 

  def __init__(self, first, last, age, community):
    super().__init__(first, last, age)
    self.community = community
    Moderator.active_mods += 1

  def remove_post(self):
    return f"{self.full_name()} removed a post from the {self.community}"

  @classmethod
  def display_active_mods(cls):
     return f"There are currently {cls.active_mods} moderators online."

user = User("Caryssa", "Perez", 24)
moderator= Moderator("Irma", "Mesa", 25, "Filming")

print(user.full_name())
print(moderator.full_name())
print(User.display_active_users())
print(Moderator.display_active_mods())
print(user.logout())
print(User.active_users)