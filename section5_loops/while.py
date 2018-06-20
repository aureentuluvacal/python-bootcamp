message = input("What's the secret password? ")

while message != "bananas":
  print("Wrong!")
  message = input("What's the secret password? ")

print("Correct!")

num = 1

while num < 11:
  print(num)
  num += 1