print("How old are you?")
age = input()

if age:
  age = int(age)

  if age >= 21:
    print("Good to enter and drink.")
  elif age >= 18: 
    print("You can enter but need a wristband.")
  else:
    print("You're way too young.")
else:
  print("You need to tell me your age. No entry.") 
