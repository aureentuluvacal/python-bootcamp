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
    print(f"There are currently {cls.active_users} users online.")

  @classmethod
  def normalize_arguments(cls, args_str):
    first, last, age = args_str.split(",")
    return cls(first, last, int(age))

user1 = User("Caryssa", "Perez", 24)
user2 = User.normalize_arguments("Irma, Mesa, 25")

print(user1.full_name())
print(user2.full_name())
print(User.display_active_users())
print(user1.logout())
print(User.active_users)